# Change Log

# 0.1.5

- Upgrade to reasoner-validator 4.2.4 with enhanced OneHop validation of fuzzy matching of identifiers against Node Normalization.
- Added the **`GraphValidationTests.test_case_processor()`** function to directly validate a previously run TRAPI Response previously. This is mainly of utility to the StandardsValidationTestRunner for now (OneHopTestRunner isn't yet fully ported to run this way). Note that creation of this mode of operation triggered a significant internal DRY code refactor of the test runner code (for which, unit tests still successfully pass)
- FULL_TEST gatekeeper environment variable now suppresses 'real asset' related tests.
- Cleaned up a bit of technical debt

# 0.1.4

- upgrade to reasoner-validator 4.2.3 with enhanced OneHop validation.

# 0.1.3

- upgrade to reasoner-validator 4.2.0
- fix bug in completely returning of result message dictionaries from test runs with a list of more than one target component
- made ARS unimplemented TRAPI query non-fatal with error messages
- TestRunner CLI defaults are set in the CLI as the current TRAPI and Biolink release SemVers, not just 'None'
- Formatted output of non-empty TestRunner error message dictionary entries sorted by message precedence: "critical" > "error" > "warning" > "skipped" > "info"

## 0.1.2

- update to reasoner-validator 4.1.5 (patches problematic biolink:treats mixin predicate validation)
- fix **`skipped.test`** report messages to align with reasoner-validator 4.1.6 validation code reporting expectations

## 0.1.1

- bug fix patch

## 0.1.0

- update to reasoner-validator 4.1.4
- fixed propagation of validation messages within StandardsValidationTest TestRunner

## 0.0.13

- anchored graph validation test classes on TRAPIResponseValidator rather than BiolinkValidator for more correct and efficient propagation of validation messages
- improved sample test asset data returns more helpful unit test TestRunner results

## 0.0.12

- repository generally renamed to graph-validation-test-runners (but propagate current version)
- renamed various TestRunner packages to have suffix "_runner"
- repair some technical debt; patch unit tests
- added get_compliance_tests() method used by TestHarness


## 0.0.11 (reissued 0.0.10)

- Update reasoner-validator to 4.1.2
- Add back in supported Python 3.9
- disable a couple of components in unit test of the Translator SmartAPI Registry (probably outdated)

## 0.0.9

- formatted test status messages converted from 2-tuple to a dictionary with "status" and "messages"
- component and environment parameters generally changed to simple strings (not testing model enums)
- constrain Python to ">=3.10,<3.12" (discovered problem with 3.12 for some code runtime situations)
- Update to 0.3.1 release of TranslatorTestingModel
- update to 4.0.2 release of reasoner-validator (which updates BMT to 1.4.2 and adds Bioregistry 0.11.0)

## 0.0.8

- update to reasoner-validator 4.0.1 (which uses Pydantic 2)
- remove reasoner-pydantic; delete the **graph_validation_test.requests** (which used reasoner-pydantic) an **graph_validation_test.utils.testsuite** modules (both unused legacy modules copied over from Benchmarks for coding inspiration)
- change some logger messages to 'debug' (from 'info')

## 0.0.7

- Removing internal generation of TestAsset identifiers, assuming that they are provided by the caller of the system, via the run_tests method, which now expects a 'test_asset_id' string argument, as does the 'build_test_asset' method.
- Reformatting the return values of various methods of the system, in particular, the **`GraphValidationTest.run_tests()`** method, to better align with Translator TestHarness expectations.

## 0.0.6

- Moved, into inside of **`graph_validation_test.get_parameters()`** method, the string parsing of CLI comma-delimited components parameter to the **`List[ComponentEnum]`** now expected as the **`components`** parameter of the **`graph_validation_test.run_tests()`** method.

## 0.0.5

- Belated upgrade to TranslatorTestingModel release 0.2.6
- Fix sample data to more credible predicate
- Tweak unit test environments to match current deployment reality
- Reactivate skipped unit tests after updating some url's to currently active endpoints

## 0.0.4 (package bug fix; deprecates v0.0.3 in pypi - yanked)

- Added missing 'graph_validation_test' to the release

## 0.0.3

- co-routine management of co-routine processing pushed up to a top level 'asyncio.run' of the highest level (now 'async') method, converting processing underneath to await runs on async methods, down to the lowest level parallel processing of co-routines of test cases
- Some Ontology KP graph and Translator endpoing access unit tests are temporarily skipped (endpoints offline on release day?)

## 0.0.2

- fixes bugs in release 0.0.1, particularly, missing parameters at the CLI level
- Python Logging removed as an explicit parameter (logging assumed configured externally by regular Python, pyproject.toml and environmental variable conventions)

## 0.0.1

- porting of legacy SRI_Testing into OneHopTest and StandardsValidationTest TestRunners in the 2024 Translator Testing framework; this version only currently supports tests test ARA and KP components (not ARS nor UI level).
- The underlying TRAPI standard is still (via reasoner-validator 4.0.0) only to release 1.4.2;
- This release runs on the latest Biolink Model release without choking but the underlying reasoner-validator module doesn't yet do any special validation of the latest Biolink Model semantic features (in 4.1.4 and beyond)
