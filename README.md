# generate-indy-pool-transactions-with-key
Generates indy pool transactions with a secret key.

## Generate Indy Pool Transactions Using the Script
1. Download the `generate_indy_pool_transactions_with_key` script:
    ```
    $ sudo curl -o /usr/local/bin/generate_indy_pool_transactions_with_key \
      https://raw.githubusercontent.com/rshuang2015/generate-indy-pool-transactions-with-key/main/generate_indy_pool_transactions_with_key
    ```
2. Apply executable permissions to the script:
    ```
    $ sudo chmod +x /usr/local/bin/generate_indy_pool_transactions_with_key
    ```
3. Execute the script with your secret key to generate keys and genesis transaction files::
    ```
    $ generate_indy_pool_transactions_with_key --clients 1 --nodes 4 --nodeNum 1 2 3 4 --key your_secret_key
    ```

## References
- https://github.com/hyperledger/indy-node
- https://github.com/hyperledger/indy-node/blob/main/scripts/generate_indy_pool_transactions
- https://github.com/hyperledger/indy-node/blob/main/docs/source/start-nodes.md
