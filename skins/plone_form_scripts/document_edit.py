## Script (Python) "document_edit"
##parameters=field_id, text_format, field_text, file='', SafetyBelt='', choice=' Change ', field_title='', field_description=''
##title=Edit a document
REQUEST=context.REQUEST
id, text, title, description = field_id, field_text, field_title, field_description

errors=context.validate_document_edit()

if errors:
    edit_form=getattr(context, context.getTypeInfo().getActionById( 'edit'))
    return edit_form()
    
context.edit( text_format
            , text
            , file=file
            , safety_belt=SafetyBelt
            )
            
if file and file.filename:
    if file.filename.find('\\')>-1:       
        id=file.filename.split('\\')[-1]
    if file.filename.find('/')>-1: 
        id=file.filename.split('/')[-1]
        
    # if id.find('.')>-1: id=id[:id.find('.')] 

if not context.isIDAutoGenerated(id): 
    context.REQUEST.set('id', id)

qst='portal_status_message=Document+changed.'

REQUEST.set('portal_status_message', 'Document+changed.')
if hasattr(context, 'extended_edit'):
    edit_hook=getattr(context,'extended_edit')
    response=edit_hook()
    if response:
        return response

target_action = context.getTypeInfo().getActionById( 'view' )

context.REQUEST.RESPONSE.redirect( '%s/%s?%s' % ( context.absolute_url()
                                                , target_action
                                                , qst
                                                ) )

