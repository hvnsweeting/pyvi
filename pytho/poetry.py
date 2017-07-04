import logging

from . import base
from .base import split_cons_vowel

logger = logging.getLogger(__name__)


# https://en.wikipedia.org/wiki/Vietnamese_language
FLAT = base.LEVEL + base.HANGING
OBLIQUE = base.SHARP + base.ASKING + base.TUMBLING + base.HEAVY


def validate_line(line, rule, wc=7):
    line = line.strip()
    words = line.split(' ')
    if len(words) != wc:
        return False

    res = [f(w) for (f, w) in zip(rule, words)]
    logger.debug(words)
    logger.debug(rule)
    logger.debug(res)
    return all(res)


def rule(notation):
    if notation == 'B':
        return flat
    elif notation == 'T':
        return oblique
    else:
        raise Exception('Unreconized notation %s' % notation)


def line_rule_from_tb(tb_line):
    '''Convert Vietnamese notation to rule'''
    notations = tb_line.split(' - ')

    return [rule(i) for i in notations]


def validate_7w4s(four_sentences, rule_notation):
    if isinstance(four_sentences, str):
        four_sentences = four_sentences.strip()
        four_sentences = four_sentences.replace(',', '').replace('.', '')
        four_sentences = four_sentences.replace('?', '').replace('!', '')
        four_sentences = four_sentences.lower()
        four_sentences = four_sentences.split('\n')

    assert len(four_sentences) == 4

    rules = [line_rule_from_tb(l.strip())
             for l in rule_notation.strip().split('\n')]

    result = [validate_line(line, rule)
              for (line, rule) in zip(four_sentences, rules)]
    logger.info('%s', four_sentences)
    logger.info('%s', result)
    return all(result)


def validate_ltvb(four_sentences):
    '''Luật trắc vần bằng

    http://www.maiyeuem.net/topic/155834/Huong-dan-lam-tho-Duong-luat-That-ngon-tu-tuyet---That-ngon-bat-cu # NOQA
    '''
    notation = '''T - T - B - B - T - T - B
                  B - B - T - T - T - B - B
                  B - B - T - T - B - B - T
                  T - T - B - B - T - T - B'''

    return validate_7w4s(four_sentences, notation)


def validate_ltvb_2v(four_sentences):
    '''Luật trắc vần bằng 2 vần'''
    notation = '''T - T - B - B - B - T - T
    B - B - T - T - T - B - B
    B - B - T - T - B - B - T
    T - T - B - B - T - T - B'''

    return validate_7w4s(four_sentences, notation)


def validate_lbvb_2v(four_sentences):
    '''Luật bằng vần bằng 2 vần'''
    notation = '''B - B - T - T - B - B - T
    T - T - B - B - T - T - B
    T - T - B - B - B - T - T
    B - B - T - T - T - B - B
    '''
    return validate_7w4s(four_sentences, notation)


def validate_lbvb(four_sentences):
    '''Luật bằng vần bằng
    '''

    notation = '''B - B - T - T - T - B - B
    T - T - B - B - T - T - B
    T - T - B - B - B - T - T
    B - B - T - T - T - B - B'''
    return validate_7w4s(four_sentences, notation)


def flat(word):
    # TODO this is no simple, so here just try a simple way
    # TODO handle triphthong/diphthong
    cons, final = split_cons_vowel(word)
    for ch in final:
        if ch in FLAT:
            return True
    return False


def oblique(word):
    # TODO
    cons, final = split_cons_vowel(word)
    for ch in final:
        if ch in OBLIQUE:
            return True
    return False


obl = oblique
