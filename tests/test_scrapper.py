from webscrapper import BaseOptions

def verify_if_return_from_processamento_is_equal_to_opt03():
    embrapa_base: BaseOptions.EmbrapaBaseOptions = BaseOptions.EmbrapaBaseOptions()
    assert embrapa_base.base_options == "opt_03"


