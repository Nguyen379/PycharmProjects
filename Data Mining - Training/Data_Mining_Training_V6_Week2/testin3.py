import re
import numpy as np
from unidecode import unidecode

letters = list("abcdefghijklmnopqrstuvwxyz"
               "áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKLMNOPQRSTUVWXYZ"
               "ÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ")
letters2 = list("abcdefghijklmnopqrstuvwxyz")
typo = {"ă": "aw", "â": "aa", "á": "as", "à": "af", "ả": "ar", "ã": "ax", "ạ": "aj", "ắ": "aws", "ổ": "oor", "ỗ": "oox",
        "ộ": "ooj", "ơ": "ow",
        "ằ": "awf", "ẳ": "awr", "ẵ": "awx", "ặ": "awj", "ó": "os", "ò": "of", "ỏ": "or", "õ": "ox", "ọ": "oj",
        "ô": "oo", "ố": "oos", "ồ": "oof",
        "ớ": "ows", "ờ": "owf", "ở": "owr", "ỡ": "owx", "ợ": "owj", "é": "es", "è": "ef", "ẻ": "er", "ẽ": "ex",
        "ẹ": "ej", "ê": "ee", "ế": "ees", "ề": "eef",
        "ể": "eer", "ễ": "eex", "ệ": "eej", "ú": "us", "ù": "uf", "ủ": "ur", "ũ": "ux", "ụ": "uj", "ư": "uw",
        "ứ": "uws", "ừ": "uwf", "ử": "uwr", "ữ": "uwx",
        "ự": "uwj", "í": "is", "ì": "if", "ỉ": "ir", "ị": "ij", "ĩ": "ix", "ý": "ys", "ỳ": "yf", "ỷ": "yr", "ỵ": "yj",
        "đ": "dd",
        "Ă": "Aw", "Â": "Aa", "Á": "As", "À": "Af", "Ả": "Ar", "Ã": "Ax", "Ạ": "Aj", "Ắ": "Aws", "Ổ": "Oor", "Ỗ": "Oox",
        "Ộ": "Ooj", "Ơ": "Ow",
        "Ằ": "AWF", "Ẳ": "Awr", "Ẵ": "Awx", "Ặ": "Awj", "Ó": "Os", "Ò": "Of", "Ỏ": "Or", "Õ": "Ox", "Ọ": "Oj",
        "Ô": "Oo", "Ố": "Oos", "Ồ": "Oof",
        "Ớ": "Ows", "Ờ": "Owf", "Ở": "Owr", "Ỡ": "Owx", "Ợ": "Owj", "É": "Es", "È": "Ef", "Ẻ": "Er", "Ẽ": "Ex",
        "Ẹ": "Ej", "Ê": "Ee", "Ế": "Ees", "Ề": "Eef",
        "Ể": "Eer", "Ễ": "Eex", "Ệ": "Eej", "Ú": "Us", "Ù": "Uf", "Ủ": "Ur", "Ũ": "Ux", "Ụ": "Uj", "Ư": "Uw",
        "Ứ": "Uws", "Ừ": "Uwf", "Ử": "Uwr", "Ữ": "Uwx",
        "Ự": "Uwj", "Í": "Is", "Ì": "If", "Ỉ": "Ir", "Ị": "Ij", "Ĩ": "Ix", "Ý": "Ys", "Ỳ": "Yf", "Ỷ": "Yr", "Ỵ": "Yj",
        "Đ": "Dd"}
region = {"ẻ": "ẽ", "ẽ": "ẻ", "ũ": "ủ", "ủ": "ũ", "ã": "ả", "ả": "ã", "ỏ": "õ", "õ": "ỏ", "i": "j"}
region2 = {"s": "x", "l": "n", "n": "l", "x": "s", "d": "gi", "S": "X", "L": "N", "N": "L", "X": "S", "Gi": "D",
           "D": "Gi"}
vowel = list("aeiouyáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵ")
acronym = {"không": "ko", " anh": " a", "em": "e", "biết": "bít", "giờ": "h", "gì": "j", "muốn": "mún", "học": "hok",
           "yêu": "iu",
           "chồng": "ck", "vợ": "vk", " ông": " ô", "được": "đc", "tôi": "t",
           "Không": "Ko", " Anh": " A", "Em": "E", "Biết": "Bít", "Giờ": "H", "Gì": "J", "Muốn": "Mún", "Học": "Hok",
           "Yêu": "Iu",
           "Chồng": "Ck", "Vợ": "Vk", " Ông": " Ô", "Được": "Đc", "Tôi": "T", }
teen = {"ch": "ck", "ph": "f", "th": "tk", "nh": "nk",
        "Ch": "Ck", "Ph": "F", "Th": "Tk", "Nh": "Nk"}

original_word = "nguyeen"
reverse_typo = {v: k for k, v in typo.items()}


def edit_original_word(original_word):
    edit_original_word = original_word
    for fault in reverse_typo:
        if fault in edit_original_word:
            edit_original_word = original_word.replace(fault, reverse_typo[fault])
    return edit_original_word


print(edit_original_word("booj"))
