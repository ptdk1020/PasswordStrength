This folder contains a few old scripts that I previously used to extract information from the password dataset. Most of these weren't used in the current product, but are still useful for reference and re-usability.

- `feature_maps` contains functions that serve to extract password information such as number of uppercase letters, number of lowercase letters, number of unique characters, etc.
- `features_script` applies functions from `features_maps` to record password information in a pandas dataframe. 
- `zxcvbn_features` records useful information computed through [zxcvbn](https://github.com/dropbox/zxcvbn).