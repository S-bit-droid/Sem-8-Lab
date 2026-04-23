<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template match="/">

<html>
<head>
    <title>CD Catalog</title>
    <style>
        table {
            border-collapse: collapse;
            width: 80%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>
    <h2>CD Catalog</h2>

    <table>
        <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Country</th>
            <th>Company</th>
            <th>Price</th>
            <th>Year</th>
        </tr>

        <xsl:for-each select="catalog/cd">
            <tr>
                <td><xsl:value-of select="title"/></td>
                <td><xsl:value-of select="artist"/></td>
                <td><xsl:value-of select="country"/></td>
                <td><xsl:value-of select="company"/></td>
                <td><xsl:value-of select="price"/></td>
                <td><xsl:value-of select="year"/></td>
            </tr>
        </xsl:for-each>

    </table>

</body>
</html>

</xsl:template>

</xsl:stylesheet>