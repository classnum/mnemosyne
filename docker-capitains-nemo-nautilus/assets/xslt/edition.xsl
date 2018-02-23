<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:t="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="t">

  <!-- glyphs -->
  <xsl:include href="teig.xsl" />


  <xsl:template match="t:div[@type = 'edition']">
    <div id="edition">
      <xsl:attribute name="class">
        <xsl:text>edition lang_</xsl:text>
        <xsl:value-of select="@xml:lang"/>
      </xsl:attribute>
      <xsl:apply-templates/>
    </div>
  </xsl:template>
  
  <xsl:template match="t:div[@type = 'textpart']">
    <xsl:element name="div">
      <xsl:attribute name="class">
        <xsl:value-of select="@subtype" />
      </xsl:attribute>
      <xsl:choose>
        <xsl:when test="child::t:l">
          <ol><xsl:apply-templates /></ol>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:element>
  </xsl:template>
  
  <xsl:template match="t:l">
    <xsl:element name="li">
      <xsl:attribute name="value"><xsl:value-of select="@n"/></xsl:attribute>
      <xsl:apply-templates/>
    </xsl:element>
  </xsl:template>
  
  <xsl:template match="t:pb">
    <div class='pb'><xsl:value-of select="@n"/></div>
  </xsl:template>
  
  <xsl:template match="t:ab/text()">
    <xsl:value-of select="." />
  </xsl:template>
  
  
  <xsl:template match="t:p">
    <p>
      <xsl:apply-templates/>
    </p>
  </xsl:template>


  <xsl:template match="t:lb" />
  
  
  <xsl:template match="t:ex">
  	<span class="ex">
    	<xsl:text>(</xsl:text><xsl:value-of select="." /><xsl:text>)</xsl:text>
    </span>
  </xsl:template>
  
  <xsl:template match="t:abbr">
  	<span class="abbr">
    	<xsl:text></xsl:text><xsl:value-of select="." /><xsl:text></xsl:text>
    </span>
  </xsl:template>  
  
  <xsl:template match="t:gap">
    <span class="gap">
      <xsl:choose>
        <xsl:when test="@quantity and @unit='character'">
          <xsl:value-of select="string(@quantity)" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>---</xsl:text>
        </xsl:otherwise>
      </xsl:choose>

    </span>
  </xsl:template>
  
  <xsl:template match="t:head">
  </xsl:template>
  
  <xsl:template match="t:sp">
    <section class="speak">
      <xsl:if test="./t:speaker">
        <em><xsl:value-of select="./t:speaker/text()" /></em>
      </xsl:if>
      <ol>
        <xsl:apply-templates select="./t:l"/>
      </ol>
    </section>
  </xsl:template>
  
  <xsl:template match="t:supplied">
    <span>
      <xsl:attribute name="class">supplied supplied_<xsl:value-of select='@cert' /></xsl:attribute>
      <xsl:text>[</xsl:text>
      <xsl:apply-templates/><xsl:if test="@cert = 'low'"><xsl:text>?</xsl:text></xsl:if>
      <xsl:text>]</xsl:text>
    </span>
  </xsl:template>  
  
  <xsl:template match="t:note">
    <span class="note"><a href="#">[*]</a><span class="note-content"><xsl:text>(</xsl:text><xsl:value-of select="." /><xsl:text>)</xsl:text></span></span>
  </xsl:template>
  
  <xsl:template match="t:choice">
    <span class="choice">
      <xsl:attribute name="title">
        <xsl:value-of select="reg" />
      </xsl:attribute>
      <xsl:value-of select="orig" /><xsl:text> </xsl:text>
    </span>
  </xsl:template>

  <xsl:template match="t:unclear">
    <span class="unclear"><xsl:value-of select="." /></span>
  </xsl:template>

  
</xsl:stylesheet>
