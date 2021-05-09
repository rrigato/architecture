# react_docs_test_steps

1) jest test runner to render to jsdom
2) Setup react component tree to DOM with beforeEach
3) render component you want to test using the act function from react-dom/test-utils
4) assert expected DOM UI output
5) Tear down react component tree with afterEach
