from exceptions import InvalidCNPJError

def validate_cnpj(cnpj):
    if len(cnpj)==14:
        return f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    else:
        raise InvalidCNPJError(cnpj)