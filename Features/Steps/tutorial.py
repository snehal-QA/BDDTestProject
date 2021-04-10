from behave import *


@given(u'we have behave installed')
def step_impl(context):
    pass

@when(u'we implement a test')
def step_impl(context):
    assert True is not False


@then(u'behave will test it for us!')
def step_impl(context):
    assert context.failed is False

# @given(u'a number <a>')
# def step_impl(context,a):
#     return a
#
#
# @given(u'a number "{b}"')
# def step_impl(context,b):
#     return b
#
#
# @when(u'addition is performed on a & b')
# def step_impl(context,a,b):
#     return a+b
#
#
# @then(u'sum of number is a+b')
# def step_impl(context):
#     assert 8==8

