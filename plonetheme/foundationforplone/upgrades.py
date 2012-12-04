from Products.CMFCore.utils import getToolByName
PROFILEID = 'profile-plonetheme.foundationforplone:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILEID)
