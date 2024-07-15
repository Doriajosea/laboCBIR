from descriptor import glcm, bitdesc
from distances import manhattan, euclidean, chebyshev, canberra

path = '../datasets/test.png'
patha = '../datasets/testa.png'
pathb = '../datasets/testb.png'
pathc = '../datasets/testc.png'
pathd = '../datasets/testd.png'
pathe = '../datasets/teste.jpg'
pathf = '../datasets/testf.jpg'



def main():
    
    feat_path = glcm(path)
    feat_patha = glcm(patha)
    feat_pathb = glcm(pathb)
    feat_pathc = glcm(pathc)
    feat_pathd = glcm(pathd)
    feat_pathe = glcm(pathe)
    feat_pathf = glcm(pathf)
    print(f'''\nManhattan: {manhattan(feat_path, feat_patha)} | {manhattan(feat_path, feat_pathb)} | {manhattan(feat_path, feat_pathc)} | {manhattan(feat_path, feat_pathd)} | {manhattan(feat_path, feat_pathe)} | {manhattan(feat_path, feat_pathf)}\n
                         Euclidean: {euclidean(feat_path, feat_patha)} | {euclidean(feat_path, feat_pathb)} | {euclidean(feat_path, feat_pathc)} | {euclidean(feat_path, feat_pathd)} | {euclidean(feat_path, feat_pathe)} | {euclidean(feat_path, feat_pathf)}\n
                         Chebyshev: {chebyshev(feat_path, feat_patha)} | {chebyshev(feat_path, feat_pathb)} | {chebyshev(feat_path, feat_pathc)} | {chebyshev(feat_path, feat_pathd)} | {chebyshev(feat_path, feat_pathe)} | {chebyshev(feat_path, feat_pathf)}\n
                         Canberra: {canberra(feat_path, feat_patha)} | {canberra(feat_path, feat_pathb)} | {canberra(feat_path, feat_pathc)} | {canberra(feat_path, feat_pathd)} | {canberra(feat_path, feat_pathe)} | {canberra(feat_path, feat_pathf)}\n
                            ''')

if __name__ == '__main__':
    main()