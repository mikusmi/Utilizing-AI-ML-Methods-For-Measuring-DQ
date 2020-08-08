Experiment 1 – Autoencoder
===

An approach with elementary Autoencoder models was chosen in order
to detect anomalies. An autoencoder model is trained for each dataset feature.
This setting allows us to record the reconstruction error for the desired value in
a feature as well as the total reconstruction error for an entire row. The input
values of the autoencoder were tokenized text values converted to a numerical
representation. This approach was able to detect approximately half of the
manually created synthetic data quality defects on both datasets. Several potential
data quality defects contained in the original dataset were found as well.
The advantage of this approach is in its automation (only one essential parameter
for defining the reconstruction error threshold is needed) and in its application
on heterogeneous attributes. The alternative non-AI approach, where
a regular expression was defined for format checking, has found all wrong records
in a given data feature, but is task-dependent, requires expert knowledge
and manual effort. As part of the extension of the Autoencoder approach, it
would be appropriate to implement more advanced Autoencoders models (e.g.
VAE) and additional metrics that would assess whether a given entire record
is a suitable adept for data quality control as well as with other methods for
semantic representation which would adequately represent the structure autoencoder
input features. To the best of author’s knowledge, this approach is
not described in any existing literature nor it is implemented in existing data
quality tools. Detail information about experiment can be found in the Master's thesis (3.3.1 Experiment 1 – Autoencoder).
