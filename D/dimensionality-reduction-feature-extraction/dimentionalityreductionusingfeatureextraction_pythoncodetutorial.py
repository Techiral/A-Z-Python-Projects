# -*- coding: utf-8 -*-
"""DimentionalityReductionUsingFeatureExtraction_PythonCodeTutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KIR85hqoxb0VCiX8KipjZeb21cNPfDXN
"""

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA, KernelPCA
from sklearn.datasets import make_circles
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import NMF
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix

# Load the data
digits = datasets.load_digits()
# Feature matrix standardization
features = StandardScaler().fit_transform(digits.data)
# Perform PCA While retaining 80% of variance
pca = PCA(n_components=0.95, whiten=True)
# perform PCA
pcafeatures = pca.fit_transform(features)
# Display results
print("Original number of features:", features.shape[1])
print("Reduced number of features:", pcafeatures.shape[1])

# Creation of the linearly inseparable data
features, _ = make_circles(n_samples=2000, random_state=1, noise=0.1, factor=0.1)
# kernal PCA with radius basis function (RBF) kernel application
k_pca = KernelPCA(kernel="rbf", gamma=16, n_components=1)
k_pcaf = k_pca.fit_transform(features)
print("Original number of features:", features.shape[1])
print("Reduced number of features:", k_pcaf.shape[1])

#flower dataset loading:
iris = datasets.load_iris()
features = iris.data
target = iris.target
# Creation of LDA. Use of LDA for features transformation
lda = LinearDiscriminantAnalysis(n_components=1)
features_lda = lda.fit(features, target).transform(features)
# Print the number of features
print("number of features(original):", features.shape[1])
print("number of features that was reduced:", features_lda.shape[1])

lda.explained_variance_ratio_

# Load Iris flower dataset:
iris123 = datasets.load_iris()
features = iris123.data
target = iris123.target
# Create and run LDA
lda_r = LinearDiscriminantAnalysis(n_components=None)
features_lda = lda_r.fit(features, target)
# array of explained variance ratios
lda_var_r = lda_r.explained_variance_ratio_
# function ceration
def select_n_c(v_ratio, g_var: float) -> int:
    # initial variance explained setting
    total_v = 0.0
    # number of features initialisation
    n_components = 0
    # If we consider explained variance of each feature:
    for explained_v in v_ratio:
        # explained variance addition to the total
        total_v += explained_v
        # add one to number of components
        n_components += 1
        # we attain our goal level of explained variance
        if total_v >= g_var:
            # end the loop
            break
    # return the number of components
    return n_components

# run the function
select_n_c(lda_var_r, 0.95)

# data loading
digit = datasets.load_digits()
# feature matrix loading
feature_m = digit.data
# Creation, fit and application of NMF
n_mf = NMF(n_components=12, random_state=1)
features_nmf = n_mf.fit_transform(feature_m)
# Show results
print("Original number of features:", feature_m.shape[1])
print("Reduced number of features:", features_nmf.shape[1])

# data loading
digit123 = datasets.load_digits()
#  feature matrix Standardization
features_m = StandardScaler().fit_transform(digit123.data)
# sparse matrix creation
f_sparse = csr_matrix(features_m)
# TSVD creation
tsvd = TruncatedSVD(n_components=12)
# sparse matrix TSVD
features_sp_tsvd = tsvd.fit(f_sparse).transform(f_sparse)
# results
print("Original number of features:", f_sparse.shape[1])
print("Reduced number of features:", features_sp_tsvd.shape[1])

# Sum of first three components' explained variance ratios
tsvd.explained_variance_ratio_[0:3].sum()

