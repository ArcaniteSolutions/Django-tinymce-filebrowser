function mce_filebrowser(field_name, url, type, win) {
    // document.domain = SETTINGS.get("DOCUMENT_DOMAIN");//this is to allow cross subdomain loading of popups
    
    tinyMCE.activeEditor.windowManager.open({
        url: "/mce_filebrowser/" + type + "/",
        title: 'Insert media',
        width: 550,
        height: 300
    }, {
        window : win,
        input : field_name
    });  
}
