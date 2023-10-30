import logging
import re


class SensitiveDataFilter(logging.Filter):
    def filter(self, record: logging.LogRecord):
        card_number = re.search(r'number": "(\d{16})', record.msg)
        if card_number:
            card_number_masked = re.sub(
                r'(\d{6}).*(\d{4})', r'\1********\2', card_number[1]
            )
            record.msg = record.msg.replace(card_number[1], card_number_masked)
            card_cvv = re.search(r'cvc": "(\d{4}|\d{3})', record.msg)
            if card_cvv:
                record.msg = record.msg.replace(card_cvv[0], 'cvc": "***')
            card_exp = re.search(r'expiryYear": "(\d{4})', record.msg)
            if card_exp:
                record.msg = record.msg.replace(card_exp[0], 'expiryYear": "****')
            holder_name = re.search(r'holderName": "(.*?)"', record.msg)
            if holder_name:
                holder_name_masked = ''
                for name in holder_name[1].split(' '):
                    holder_name_masked += '{} '.format(
                        name[0 : round(len(name) / 2)].ljust(len(name), '*')
                    )
                record.msg = record.msg.replace(holder_name[1], holder_name_masked)
        return True
