def extract_paper(paper_file_path: str, font_size: int) -> dict:
    f = open(paper_file_path, 'r').read()
    result = {'title': f.split('\n')[0] + '\n',
              'abstract': f[f.find('ABSTRACT'):f.find('KEYWORDS')],
              'keywords': f[f.find('keywords'):f.find('INTRODUCTION')].split(','),
              'introduction': f[f.find('introduction'):f.find('BODY')],
              'BODY': f[f.find('BODY'):f.find('CONCLUSION')],
              'conclusion': f[f.find('conclusion'):f.find('REFERENCES')],
              'references': [i.split(']')[1] for i in f[f.find('REFERENCES'):].split('\n')],
              'words_count': len(f.split(' ')) + len(f.split('\n')) - 8}

    result['pages_count'] = int(result['words_count']/int(512/int(font_size/16)))
    if result['pages_count'] % 1 > 0:
        result['pages_count'] = int(result['pages_count']) + 1

    if (len(result['abstract'].split(' '))+len(result['abstract'].split('\n'))) > 150:
        raise Exception("The abstract section can't be more than 150 words")
    if len(result['keywords']) > 5:
        raise Exception("You can't put more than 5 keywords")
    if sorted(result['keywords']) != result['keywords']:
        raise Exception("Keywords are not sorted")
    if result['pages_count'] > 9:
        raise Exception("The whole paper can't be more than 9 pages")

    return result
