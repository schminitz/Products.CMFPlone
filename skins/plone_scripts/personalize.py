## Script (Python) "personalize"
##title=Personalization Handler.
##bind namespace=_
##parameters=portrait=None
REQUEST=context.REQUEST
portrait_id='MyPortrait'
context.portal_registration.setProperties(REQUEST)

if REQUEST.has_key('portal_skin'):
    context.portal_skins.updateSkinCookie()
    
qs = '/personalize_form?portal_status_message=Member+changed.'

#if a portait file was upload put it in the /Members/XXXX/.personal/MyPortrait
if portrait and portrait.filename:
    
    personal=context.getPlonePersonalFolder()

    if not personal:
        home=context.portal_membership.getHomeFolder()
        home.manage_addProduct['CMFCore'].manage_addContent(type='Portal Folder', id='.personal')
        personal=getattr(home, '.personal')

    if not hasattr(personal, portrait_id):
        personal.invokeFactory(type_name='Image', id=portrait_id)
    
    portrait_obj=getattr(personal, portrait_id, None)
    portrait_obj.edit(file=portrait)


context.REQUEST.RESPONSE.redirect(context.portal_url() + qs)
