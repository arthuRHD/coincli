# Coincli

Unofficial Coinbase CLI tools based on Coinbase v2 API

## Install

```sh
pip install coincli
```

### What's next ?

- Buying/selling with the payment method of choice
- Cryptocurrencies swapping
- Alerting at certain prices

These will be implemented before June 2021

## Usage

```sh
coincli balance ETH # Display your ETH Balance in €
coincli price BTC # Display the BTC sell and buy prices
coincli wallet LTC # Display your coinbase LTC wallet data (id, creation date, balance, name)
```

## Config

This is the configuration template

```ini
[coinbase]
public = my_api_key
private = my_private_key
```

You can get your keys on the Coinbase webapp, however it takes 48hr to unlock it.

There is two ways of using this tool:

1. Overwriting the default `config.ini` file from source code and then use it normally.
2. Importing your configurations from terminal with the argument `--config`.

```sh
coincli --config ./my_custom_config.ini balance ETH
```

## Developement

```sh
pip install -e .
```
