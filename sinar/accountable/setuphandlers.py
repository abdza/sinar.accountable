from collective.grok import gs
from sinar.accountable import MessageFactory as _

@gs.importstep(
    name=u'sinar.accountable', 
    title=_('sinar.accountable import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.accountable.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
