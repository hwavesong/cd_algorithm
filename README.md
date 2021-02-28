This project hosts the official implementation for our ICONIP 2020 paper:

Learning Discrete Sentence Representations via Construction & Decomposition [Springer Link](https://link.springer.com/chapter/10.1007/978-3-030-63830-6_66).

## Abstract
In this paper, we address the problem of learning low-dimensional, discrete representations of real-valued vectors. We propose a new algorithm called similarity matrix construction and decomposition (C\&D). In the preparation phase, we constructively generate a set of consistent, unbiased and comprehensive anchor vectors, and obtain their low-dimensional forms with PCA. The C\&D algorithm learns the discrete representations of vectors in batches. For a batch of input vectors, we first construct a similarity matrix between them and the anchor vectors, and then learn their discrete representations from the similarity matrix decomposition, where the low-dimensional forms of the anchor vectors are regarded as a fixed factor of the similarity matrix. The matrix decomposition is a mixed-integer optimization problem. We obtain the optimal solution for each bit with mathematical derivation, and then use the discrete coordinate descent method to solve it. The C\&D algorithm does not learn directly discrete representations from the input vectors, which distinguishes it from other discrete learning algorithms. We evaluate the C\&D algorithm on sentence embedding compression tasks. Extensively experimental results reveal the C\&D algorithm outperforms the latest 4 methods and reaches state-of-the-art. Detailed analysis and ablation study further validate the rationality of the C\&D algorithm.

## Usage
The experimental environment of C&D algorithm is consistent with [Shen et al..](https://github.com/Linear95/BinarySentEmb) This means that using this repository requires 3 simple steps:
1. Set up the experimental environment according to the [Shen et al.](https://github.com/Linear95/BinarySentEmb) instructions.
1. Add the CDBinEncoder class in discrete_encoders.py to the file with the same name in the [repository](https://github.com/Linear95/BinarySentEmb).
1. Modify the evaluate.py in [repository](https://github.com/Linear95/BinarySentEmb) to evaluate the C&D algorithm.

## Citation
If you find our work or code useful in your research, please consider citing:
'''
@inproceedings{DBLP:conf/iconip/SongZL20,
  author    = {Haohao Song and
               Dongsheng Zou and
               Weijia Li},
  editor    = {Haiqin Yang and
               Kitsuchart Pasupa and
               Andrew Chi{-}Sing Leung and
               James T. Kwok and
               Jonathan H. Chan and
               Irwin King},
  title     = {Learning Discrete Sentence Representations via Construction {\&}
               Decomposition},
  booktitle = {Neural Information Processing - 27th International Conference, {ICONIP}
               2020, Bangkok, Thailand, November 23-27, 2020, Proceedings, Part {I}},
  series    = {Lecture Notes in Computer Science},
  volume    = {12532},
  pages     = {786--798},
  publisher = {Springer},
  year      = {2020},
  url       = {https://doi.org/10.1007/978-3-030-63830-6\_66},
  doi       = {10.1007/978-3-030-63830-6\_66},
  timestamp = {Fri, 20 Nov 2020 12:41:31 +0100}
}
'''
If you have any questions, please contact me via issue or [email](songhaohao2018@cqu.edu.cn).


