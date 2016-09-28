<xsl:stylesheet xmlns="http://www.w3.org/1999/xhtml" xmlns:example="http://www.tei-c.org/ns/Examples" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei" version="1.0"><!-- <xsl:strip-space elements="*"/>-->
    <xsl:output method="html" version="5.0"
        encoding="UTF-8" indent="yes"/>
    <xsl:param name="ref"/><!--
##################################
### Seitenlayout und -struktur ###
##################################
-->
<xsl:template match="/">
    <div>
        <h2>TEI-Header</h2>
        <h3>by <strong><xsl:value-of select="//tei:titleStmt//tei:author"/></strong></h3>
        <table class="table table-striped">
            <tbody>
                <tr>
                    <th>
                        <abbr title="tei:titleStmt/tei:title">Title</abbr>
                    </th>
                    <td>
                        <xsl:for-each select="//tei:fileDesc/tei:titleStmt/tei:title">
                            <xsl:apply-templates/>
                            <br/>
                        </xsl:for-each>
                    </td>
                </tr>
                <xsl:if test="//tei:msIdentifier">
                    <tr>
                        <th>
                            <abbr title="//tei:msIdentifie">Identifier</abbr>
                        </th>
                        <td>
                            <xsl:for-each select="//tei:msIdentifier/child::*">
                                <abbr>
                                    <xsl:attribute name="title">
                                        <xsl:value-of select="name()"/>
                                    </xsl:attribute>
                                    <xsl:apply-templates select="."/>
                                </abbr>
                                <br/>
                            </xsl:for-each><!--<xsl:apply-templates select="//tei:msIdentifier"/>-->
                        </td>
                    </tr>
                </xsl:if>
                <xsl:if test="//tei:msContents">
                    <tr>
                        <th>
                            <abbr title="//tei:msContents">Description</abbr>
                        </th>
                        <td>
                            <xsl:apply-templates select="//tei:msContents"/>
                        </td>
                    </tr>
                </xsl:if>
                <xsl:if test="//tei:supportDesc/tei:extent">
                    <tr>
                        <th>
                            <abbr title="//tei:supportDesc/tei:extent">Extent</abbr>
                        </th>
                        <td>
                            <xsl:apply-templates select="//tei:supportDesc/tei:extent"/>
                        </td>
                    </tr>
                </xsl:if>
                <xsl:if test="//tei:titleStmt/tei:respStmt">
                    <tr>
                        <th>
                            <abbr title="//tei:titleStmt/tei:respStmt">responsible</abbr>
                        </th>
                        <td>
                            <xsl:for-each select="//tei:titleStmt/tei:respStmt">
                                <p>
                                    <xsl:apply-templates/>
                                </p>
                            </xsl:for-each>
                        </td>
                    </tr>
                </xsl:if>
                <tr>
                    <th>
                        <abbr title="//tei:availability//tei:p[1]">License</abbr>
                    </th>
                    <td>
                        <xsl:element name="a">
                            <xsl:attribute name="href">
                                <xsl:apply-templates select="//tei:licence/@target"/>
                            </xsl:attribute>
                            <xsl:apply-templates select="//tei:availability//tei:p[1]"/>
                            <xsl:apply-templates select="//tei:availability"/>
                        </xsl:element>
                    </td>
                </tr>
            </tbody>
        </table>
        <h2>TEI-Body</h2>
        <xsl:choose>
            <xsl:when test="//tei:div[@type='text']">
                <xsl:apply-templates select="//tei:div[@type='text']"/>
            </xsl:when>
            <xsl:when test="//tei:div[@type='transcript']">
                <xsl:apply-templates select="//tei:div[@type='transcript']"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="//tei:body"/>
            </xsl:otherwise>
        </xsl:choose>
    </div>
        
    </xsl:template>
    
    <xsl:template match="*" mode="serialize">
        <xsl:text>&lt;</xsl:text>
        <xsl:value-of select="name()"/>
        <xsl:apply-templates select="@*" mode="serialize"/>
        <xsl:choose>
            <xsl:when test="node()">
                <xsl:text>&gt;</xsl:text>
                <xsl:apply-templates mode="serialize"/>
                <xsl:text>&lt;/</xsl:text>
                <xsl:value-of select="name()"/>
                <xsl:text>&gt;</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text> /&gt;</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    <xsl:template match="@*" mode="serialize">&#160;<xsl:value-of select="name()"/>
        <xsl:text>="</xsl:text>
        <xsl:value-of select="."/>
        <xsl:text>"</xsl:text>
    </xsl:template>
    <xsl:template match="tei:index">
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="tei:term">
        <span class="label label-primary">
            <xsl:apply-templates/>
        </span>&#160;
    </xsl:template>
    
    <xsl:template match="tei:gi">
        <code>&lt;<xsl:apply-templates/>&gt;</code>
    </xsl:template>
    <xsl:template match="example:egXML">
        <pre>
            <xsl:apply-templates mode="serialize"/>
        </pre>
    </xsl:template>
    <xsl:template match="tei:ref">
        <a>
            <xsl:attribute name="href">
                <xsl:value-of select="./@target"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </a>
    </xsl:template>
    <xsl:template match="tei:list">
        <ul>
            <xsl:apply-templates/>
        </ul>
    </xsl:template>
    <xsl:template match="tei:item">
        <li>
            <xsl:apply-templates/>
        </li>
    </xsl:template>
    
    
    <!--
    #####################
    ###  Formatierung ###
    #####################
--><!-- opener    -->
    <xsl:template match="tei:opener">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template><!-- salute -->
    <xsl:template match="tei:salute">
        <h4>
            <xsl:apply-templates/>
        </h4>
    </xsl:template><!-- closer -->
    <xsl:template match="tei:closer">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template><!--dateline-->
    <xsl:template match="tei:dateline">
        <p align="right">
            <xsl:apply-templates/>
        </p>
    </xsl:template><!-- resp -->
    <xsl:template match="tei:respStmt/tei:resp">
        <xsl:apply-templates/>&#160;
    </xsl:template>
    <xsl:template match="tei:respStmt/tei:name">
        <xsl:for-each select=".">
            <li>
                <xsl:apply-templates/>
            </li>
        </xsl:for-each>
    </xsl:template><!-- reference strings   -->
    <xsl:template match="tei:rs[@ref or @key]">
        <strong>
            <xsl:element name="a">
                <xsl:attribute name="class">reference</xsl:attribute>
                <xsl:attribute name="data-type">
                    <xsl:value-of select="concat('list', @type, '.xml')"/>
                </xsl:attribute>
                <xsl:attribute name="data-key">
                    <xsl:value-of select="substring-after(@ref, '#')"/>
                    <xsl:value-of select="@key"/>
                </xsl:attribute>
                <xsl:value-of select="."/>
            </xsl:element>
        </strong>
    </xsl:template><!-- additions -->
    <xsl:template match="tei:add">
        <xsl:element name="span">
            <xsl:attribute name="style">
                <xsl:text>color:blue;</xsl:text>
            </xsl:attribute>
            <xsl:attribute name="title">
                <xsl:choose>
                    <xsl:when test="@place='margin'">
                        <xsl:text>zeitgenössische Ergänzung am Rand </xsl:text>(<xsl:value-of select="./@place"/>).
                    </xsl:when>
                    <xsl:when test="@place='above'">
                        <xsl:text>zeitgenössische Ergänzung oberhalb </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:when>
                    <xsl:when test="@place='below'">
                        <xsl:text>zeitgenössische Ergänzung unterhalb </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:when>
                    <xsl:when test="@place='inline'">
                        <xsl:text>zeitgenössische Ergänzung in der gleichen Zeile </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:when>
                    <xsl:when test="@place='top'">
                        <xsl:text>zeitgenössische Ergänzung am oberen Blattrand </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:when>
                    <xsl:when test="@place='bottom'">
                        <xsl:text>zeitgenössische Ergänzung am unteren Blattrand </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:text>zeitgenössische Ergänzung am unteren Blattrand </xsl:text>(<xsl:value-of select="./@place"/>)
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>
            <xsl:text/>
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template><!-- Bücher -->
    <xsl:template match="tei:bibl">
        <xsl:element name="strong">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template><!-- Seitenzahlen -->
    <xsl:template match="tei:pb">
        <xsl:element name="div">
            <xsl:attribute name="style">
                <xsl:text>text-align:right;</xsl:text>
            </xsl:attribute>
            <xsl:text>[Bl.</xsl:text>
            <xsl:value-of select="@n"/>
            <xsl:text>]</xsl:text>
        </xsl:element>
        <xsl:element name="hr"/>
    </xsl:template><!-- Tabellen -->
    <xsl:template match="tei:table">
        <xsl:element name="table">
            <xsl:attribute name="class">
                <xsl:text>table table-bordered table-striped table-condensed table-hover</xsl:text>
            </xsl:attribute>
            <xsl:element name="tbody">
                <xsl:apply-templates/>
            </xsl:element>
        </xsl:element>
    </xsl:template>
    <xsl:template match="tei:row">
        <xsl:element name="tr">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    <xsl:template match="tei:cell">
        <xsl:element name="td">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template><!-- Überschriften -->
    <xsl:template match="tei:head">
        <xsl:element name="h3">
            <xsl:element name="a">
                <xsl:attribute name="id">
                    <xsl:text>text_</xsl:text>
                    <xsl:value-of select="."/>
                </xsl:attribute>
                <xsl:attribute name="href">
                    <xsl:text>#nav_</xsl:text>
                    <xsl:value-of select="."/>
                </xsl:attribute>
                <xsl:apply-templates/>
            </xsl:element>
        </xsl:element>
    </xsl:template><!--  Quotes / Zitate -->
    <xsl:template match="tei:q">
        <xsl:element name="i">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template><!-- Zeilenumbürche   -->
    <xsl:template match="tei:lb">
        <br/>
    </xsl:template><!-- Absätze    -->
    <xsl:template match="tei:p">
        <xsl:element name="p">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template><!-- Durchstreichungen -->
    <xsl:template match="tei:del">
        <xsl:element name="strike">
            <xsl:apply-templates/>
        </xsl:element>
    </xsl:template>
    <xsl:template match="tei:w">
        <xsl:value-of select="./text()"/>
    </xsl:template>
</xsl:stylesheet>