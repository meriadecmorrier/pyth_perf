from lxml import etree

def main():
    #charge doc source
    source_doc = etree.parse("livres.xml")

    #charge styling file XSLT
    xslt_doc = etree.parse("style.xsl")

    #cree un transformateur
    transformer = etree.XSLT(xslt_doc)

    # Appliquer la transformation
    result = transformer(source_doc)

    # Ecrire le résultat dans un fichier
    with open("livres_transformed.xml", "wb") as f:
        f.write(etree.tostring(
            result,                       
            pretty_print=True,
            xml_declaration=True,
            encoding="UTF-8"
        ))

if __name__ == "__main__":
    main()