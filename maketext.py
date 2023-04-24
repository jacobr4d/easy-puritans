import sys
import collections
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(
        prog='maketext',
        description='Parse EEBO TCP XML file',
        epilog='visit https://quod.lib.umich.edu/e/eebogroup/ for more info'
    )
parser.add_argument('-c', '--chapter')
args = parser.parse_args()

def sstrip(s):
    return s.rstrip('\n') 

def printsstrip(s):
    print(sstrip(s), end='')

root = ET.fromstring(sys.stdin.read());
notes = root.findall(".//NOTE")
subnotes = root.findall(".//NOTE//*")

chapter_elts = None
if args.chapter:
    chapter_elts = root.findall(f".//*[@TYPE='chapter'][@N='{args.chapter}']") 
else:
    chapter_elts = root.findall(".//*[@TYPE='chapter']") 
    
for chapter_elt in chapter_elts:
    print()
    for f in chapter_elt.iter():
        if f in notes:
            if f.tail: printsstrip(f.tail)
        elif f in subnotes:
            continue
        elif f.tag == 'P':
            print()                         # split paragraphs
            if f.text: printsstrip(f.text)
            if f.tail: printsstrip(f.tail)
        else:
            if f.text: printsstrip(f.text)
            if f.tail: printsstrip(f.tail)


