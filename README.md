# SesameContract

SesameContract is a conditional decryption service. In order to decrypt a file,
the user must satisfy certain conditions that are set at encryption-time.
Conditions can range from lock time to passwords to multi-signature
verification.

# Tech overview

This service is inspired by the Bitcoin transaction contract.

In order to implement conditions such as lock time in a non-distributed
environment, a decentralized system of semi-trusted SesameServers is used. A
key is split into multiple parts using Shamir's secret sharing algorithm, with
each Server holding a fragment. In order to satisfy the condition, a _k_
threshold of those Servers must agree.

Other conditions (password, multi-sig verification) can be implemented in an
offline manner, in order to minimize reliance on external servers.

# Development

This project is still in a planning stage. Any existing code can only at best
be considered a proof of concept.
