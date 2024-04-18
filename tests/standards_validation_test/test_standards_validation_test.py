"""
Unit tests for Standards Validation Test code validation
"""
from sys import stderr
from typing import Dict
from json import dump
import pytest

from translator_testing_model.datamodel.pydanticmodel import TestEnvEnum, ComponentEnum
from graph_validation_test.utils.unit_test_templates import by_subject, by_object
from standards_validation_test import StandardsValidationTest, run_standards_validation_tests
from tests import SAMPLE_TEST_INPUT_1


@pytest.mark.asyncio
async def test_standards_validation_test():
    trapi_generators = [
        by_subject,
        by_object
    ]
    results: Dict = await StandardsValidationTest.run_tests(
        **SAMPLE_TEST_INPUT_1,
        trapi_generators=trapi_generators,
        environment=TestEnvEnum.prod,
        components=[
            ComponentEnum("arax"),
            ComponentEnum("molepro")
        ]
    )
    dump(results, stderr, indent=4)


# ARS tests not yet supported so yes... results will
# always be empty, with a logger message to inform why
@pytest.mark.asyncio
async def test_standards_validation_test_on_ars():
    trapi_generators = [
        by_subject,
        by_object
    ]
    results: Dict = await StandardsValidationTest.run_tests(
        **SAMPLE_TEST_INPUT_1,
        trapi_generators=trapi_generators,
        environment=TestEnvEnum.prod
    )
    assert not results


@pytest.mark.asyncio
async def test_run_standards_validation_tests():
    results: Dict = await run_standards_validation_tests(
        **SAMPLE_TEST_INPUT_1,
        environment=TestEnvEnum.prod,
        components=[
            ComponentEnum("arax"),
            ComponentEnum("molepro")
        ]
    )
    assert results
    dump(results, stderr, indent=4)
