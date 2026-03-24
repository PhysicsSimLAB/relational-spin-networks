# Encrypted references

This directory stores encrypted reference material for local use.

Rules:
- Encrypted files may be decrypted locally only when needed.
- Decrypted copies must not be committed.
- Passphrases and private keys must never be stored in the repository.

gpg --decrypt --output /tmp/rsn_framework.pdf references/encrypted/rsn_framework.pdf.gpg

/tmp/rsn_framework.pdf

rm /tmp/rsn_framework.pdf
