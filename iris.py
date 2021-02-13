#=====ライブラリ読み込み=====================================================
import numpy as np
#-----データセットを読み込むためのライブラリ-----
from sklearn import datasets
#-----正規化と標準化のためのライブラリ-----
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
#=========================================================================

#=====データセットの読み込み==================================================
iris_data = datasets.load_iris()
x1 = iris_data.data[:,0].reshape(-1,1)
x2 = iris_data.data[:,1].reshape(-1,1)
y = iris_data.target
#=========================================================================

#=====正規化===============================================================
stdsc = StandardScaler()
x1_norm = stdsc.fit_transform(x1)
x2_norm = stdsc.fit_transform(x2)
#=========================================================================

#=====標準化===============================================================
normalizer = Normalizer()
normalized_data_set = normalizer.transform(np.hstack([x1_norm , x2_norm]))
#=========================================================================

#=========================================================================
#=========================================================================

#=====量子計算部分の実装====================================================================
#-----qsharpの必要となるライブラリのオープン-----
namespace QML
{
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Math;
    open Microsoft.Quantum.Convert;
    ...
}
