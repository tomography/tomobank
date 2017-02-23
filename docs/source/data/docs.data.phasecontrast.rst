Phase Contrast
--------------

When performing in-line (propagation-based) phase-contrast X-ray tomographic measurements, images are obtained with both absorption and refraction contribution. This allows to obtain an enhanced contrast (Fresnel diffraction) at the edges of sample features  producing local phase variations. By this technique, 3D variations of the electron density in the sample can be resolved and the experiments aim at a quantitative 3D reconstruction of the complex refraction index. The recorded sample radiographs are determined by the projection of the real and imaginary part of the refractive index within the sample volume. 
The Fresnel fringes visible at the edges of the phase objects can be considered as an artefact in the reconstructed slices and should be reduced or removed before any quantitative post-processing and analysis of the images.  

Radiographs can be recorded at a single or multiple distances. If a single distance is employed, a phase retrieval algorithm is applied most often based on the homogeneity assumption and the transport of intensity equation proposed by :cite:`paganin:02`. In the case of multiple distances :cite:`cloetens:99`, the problem is afforded by using contrast transfer functions.  Because the phase-retrieval application usually produces a blurring of the reconstructed slices, it is crucial to optimize the algorithm parameters in order to obtain a good compromise between spatial resolution and discrimination of the phases of interest in the final images.

The common reconstruction approach foresees a two-steps procedure: 1) a phase-retrieval algorithm is individually applied to the acquired projections; 2) a full tomographic reconstruction is then performed using as input data the phase-retrieved projections.

add datasets ESRF01 
~~~~~~~~~~~~~~~~~~~

from https://drive.google.com/drive/folders/0B78bW1AwveI_WVdXQlBRMVBKQk0

add datasets SLS01 
~~~~~~~~~~~~~~~~~~

from https://drive.google.com/drive/folders/0B78bW1AwveI_WVdXQlBRMVBKQk0

add datasets Elettra01 
~~~~~~~~~~~~~~~~~~~~~~

from https://drive.google.com/drive/folders/0B78bW1AwveI_WVdXQlBRMVBKQk0