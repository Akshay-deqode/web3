import pytest

from web3._utils.contracts import (
    validate_payable,
)
from web3.contract import (
    parse_block_identifier_int,
)


#  This tests negative block number identifiers, which behave like python
#  list slices, with -1 being the latest block and -2 being the block before that.
#  This test is necessary because transaction calls allow negative block indexes, although
#  get_block() does not allow negative block identifiers. Support for negative block identifier
#  will likely be removed in v5.
def test_parse_block_identifier_int(web3):
    last_num = web3.eth.get_block('latest').number
    assert 0 == parse_block_identifier_int(web3, -1 - last_num)


@pytest.mark.parametrize("value", (0, "0x0", "0x00"))
def test_validate_payable(value):
    tx = {"value": value}
    abi = {"payable": False}
    validate_payable(tx, abi)
