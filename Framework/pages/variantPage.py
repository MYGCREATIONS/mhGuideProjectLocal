# -*- encoding: utf-8 -*-
"""
Created on Fri Jun 22 13:46:04 2018

@author: mdcayoglu
"""

from features.terrain import *
from Framework.common.locators import CreateVariantLocators, DashboardLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class CreateVariant:

    def __init__(self):
        self.cvL = CreateVariantLocators()
        self.dashL = DashboardLocators()

    def verifyManageAdditionalTestResults(self):
        try:
            self.driver.find_element(self.cvL.verifierManageAdditionalTestResults)
        except NoSuchElementException:
            return False
        return True

    def clickAddAnotherBiomarker(self):
        addBiomarker = explicitWaitClickable(self.cvL.addAnotherBiomarker)
        addBiomarker.click()

    def typeVariantLineage(self, variantLineage, biomarker):
        vl = world.variantdata[biomarker]['variant_lineage']
        x = explicitWaitVisibility(variantLineage)
        x.send_keys(vl)
        x.send_keys(Keys.ENTER)

    def typeDetailedVariantType(self, detailedVariantType, biomarker):
        dvt = world.variantdata[biomarker]['detailed_variant_type']
        x = explicitWaitVisibility(detailedVariantType)
        x.send_keys(dvt)
        x.send_keys(Keys.ENTER)

    def typeAssayType(self, assayType, biomarker):
        at = world.variantdata[biomarker]['assay_type']
        x = explicitWaitVisibility(assayType)
        x.send_keys(at)
        x.send_keys(Keys.ENTER)

    def typeGeneField(self, geneField, biomarker):
        gf = world.variantdata[biomarker]['gene']
        x = explicitWaitVisibility(geneField)
        x.send_keys(gf)
        x.send_keys(Keys.ENTER)

    def typeGeneFieldPartner(self, geneFieldPartner, biomarker):
        gfp = world.variantdata[biomarker]['gene_field_partner']
        x = explicitWaitVisibility(geneFieldPartner)
        x.send_keys(gfp)
        x.send_keys(Keys.ENTER)

    def typeComment(self, commentBox, biomarker):
        cm = world.variantdata[biomarker]['comment']
        x = explicitWaitVisibility(commentBox)
        x.send_keys(cm)

    def typeDetailedTypeOfGeneExpression(self, detailedTypeOfGeneExpression, biomarker):
        dt = world.variantdata[biomarker]['detailed_type_gene_expression']
        x = explicitWaitVisibility(detailedTypeOfGeneExpression)
        x.send_keys(dt)
        x.send_keys(Keys.ENTER)

    def typeDetailedTypeOfMicrosatelliteInstability(self, detailedTypeOfMicrosatelliteInstability, biomarker):
        mi = world.variantdata[biomarker]['detailed_type_microsatellite_instability']
        x = explicitWaitVisibility(detailedTypeOfMicrosatelliteInstability)
        x.send_keys(mi)
        x.send_keys(Keys.ENTER)

    def typeDetailedTypeOfProteinExpression(self, detailedTypeOfProteinExpression, biomarker):
        pe = world.variantdata[biomarker]['detailed_type_protein_expression']
        x = explicitWaitVisibility(detailedTypeOfProteinExpression)
        x.send_keys(pe)
        x.send_keys(Keys.ENTER)

    def typeDetailedTypeOfMutationalBurden(self, detailedTypeOfTumorMutationalBurden, biomarker):
        mb = world.variantdata[biomarker]['detailed_type_mutational_burden']
        x = explicitWaitVisibility(detailedTypeOfTumorMutationalBurden)
        x.send_keys(mb)
        x.send_keys(Keys.ENTER)

    def typeFirstDeletedAminoAcid(self, firstDeletedAminoAcid, biomarker):
        fd = world.variantdata[biomarker]['first_deleted_amino_acid']
        x = explicitWaitVisibility(firstDeletedAminoAcid)
        x.send_keys(fd)
        x.send_keys(Keys.ENTER)

    def typeLastDeletedAminoAcid(self, lastDeletedAminoAcid, biomarker):
        fd = world.variantdata[biomarker]['first_deleted_amino_acid']
        x = explicitWaitVisibility(lastDeletedAminoAcid)
        x.send_keys(fd)
        x.send_keys(Keys.ENTER)

    def typeHgvsVariantSymbol(self, hgvsVariantSymbol, biomarker):
        hgvs = world.variantdata[biomarker]['hgvs_variant_symbol']
        x = explicitWaitVisibility(hgvsVariantSymbol)
        x.send_keys(hgvs)
        x.send_keys(Keys.ENTER)

    def typeHgvsProteinVariant(self, hgvsProteinVariant, biomarker):
        hgvs = world.variantdata[biomarker]['hgvs_protein_variant']
        x = explicitWaitVisibility(hgvsProteinVariant)
        x.send_keys(hgvs)
        x.send_keys(Keys.ENTER)

    def typeAlternateAminoAcid(self, alternateAminoAcid, biomarker):
        aaa = world.variantdata[biomarker]['alternate_amino_acid']
        x = explicitWaitVisibility(alternateAminoAcid)
        x.send_keys(aaa)
        x.send_keys(Keys.ENTER)

    def typeAminoAcidPosition(self, aminoAcidPosition, biomarker):
        aap = world.variantdata[biomarker]['amino_acid_position']
        x = explicitWaitVisibility(aminoAcidPosition)
        x.send_keys(aap)
        x.send_keys(Keys.ENTER)

    def createVariant(self, biomarker):
        # locators start
        cv = CreateVariantLocators()
        geneField = cv.parseGeneField(biomarker)
        geneFieldPartner = cv.parseGeneFieldPartner(biomarker)
        geneFieldPartnerWild = cv.parseGeneFieldPartnerWild(biomarker)
        variantLineage = cv.parseVariantLineage(biomarker)
        aminoAcidPosition = cv.parseAminoAcidPosition(biomarker)
        alternateAminoAcid = cv.parseAlternateAminoAcid(biomarker)
        hgvsVariantSymbol = cv.parseHgvsVariantSymbol(biomarker)
        hgvsProteinVariant = cv.parseHgvsProteinVariant(biomarker)
        commentBox = cv.parseCommentBox(biomarker)
        assayType = cv.parseAssayType(biomarker)
        firstDeletedAminoAcid = cv.parseFirstDeletedAminoAcid(biomarker)
        lastDeletedAminoAcid = cv.parseLastDeletedAminoAcid(biomarker)
        prematureStopSlider = cv.parsePrematureStopSlider(biomarker)
        rearrangementOfGeneSlider = cv.parseRearrangementOfGeneSlider(biomarker)
        detailedVariantType = cv.parseDetailedVariantType(biomarker)
        detailedTypeOfGeneExpression = cv.parseDetailedTypeOfGeneExpression(biomarker)
        detailedTypeOfMicrosatelliteInstability = cv.parseDetailedTypeOfMicrosatelliteInstability(biomarker)
        detailedTypeOfProteinExpression = cv.parseDetailedTypeOfProteinExpression(biomarker)
        detailedTypeOfTumorMutationalBurden = cv.parseDetailedTypeOfTumorMutationalBurdern(biomarker)
        alternateAminoAcidIns = cv.parseAlternateAminoAcidIns(biomarker)
        # locators end
        explicitWaitVisibility(self.cvL.biomarkerType)

        if biomarker == 'gene_expression' or 'protein_expression' or 'wild_type':
            newstr = biomarker.replace('_', ' ')
            explicitWaitVisibility(self.cvL.biomarkerType).send_keys(newstr)
        else:
            explicitWaitVisibility(self.cvL.biomarkerType).send_keys(biomarker)
        explicitWaitVisibility(self.cvL.biomarkerType).send_keys(Keys.ENTER)
        if biomarker not in ['TMB', 'MSI', 'wild_type']:
            explicitWaitVisibility(geneField)
            self.typeGeneField(geneField, biomarker)
            if biomarker == 'SNV':
                self.typeAminoAcidPosition(aminoAcidPosition, biomarker)
                self.typeAlternateAminoAcid(alternateAminoAcid, biomarker)
                self.typeHgvsVariantSymbol(hgvsVariantSymbol, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'CNA':
                self.typeDetailedVariantType(detailedVariantType, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'del':
                self.typeFirstDeletedAminoAcid(firstDeletedAminoAcid, biomarker)
                self.typeLastDeletedAminoAcid(lastDeletedAminoAcid, biomarker)
                if world.variantdata[biomarker]['premature_stop'] == 'on':
                    explicitWaitClickable(prematureStopSlider).click()
                self.typeHgvsProteinVariant(hgvsProteinVariant, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'frameshift':
                self.typeAminoAcidPosition(aminoAcidPosition, biomarker)
                self.typeHgvsProteinVariant(hgvsProteinVariant, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'fusion':
                self.typeGeneFieldPartner(geneFieldPartner, biomarker)
                if world.variantdata[biomarker]['rearrangement_of_gene'] == 'on':
                    explicitWaitClickable(rearrangementOfGeneSlider).click()
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'gene_expression':
                self.typeDetailedTypeOfGeneExpression(detailedTypeOfGeneExpression, biomarker)

            if biomarker == 'indel':
                self.typeFirstDeletedAminoAcid(firstDeletedAminoAcid, biomarker)
                self.typeLastDeletedAminoAcid(lastDeletedAminoAcid, biomarker)
                self.typeAlternateAminoAcid(alternateAminoAcid, biomarker)
                self.typeHgvsProteinVariant(hgvsProteinVariant, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'ins':
                self.typeAminoAcidPosition(aminoAcidPosition, biomarker)
                self.typeAlternateAminoAcid(alternateAminoAcidIns, biomarker)
                self.typeHgvsProteinVariant(hgvsProteinVariant, biomarker)
                self.typeVariantLineage(variantLineage, biomarker)

            if biomarker == 'methylation':
                self.typeDetailedVariantType(detailedVariantType, biomarker)

            if biomarker == 'protein_expression':
                self.typeDetailedTypeOfProteinExpression(detailedTypeOfProteinExpression, biomarker)

        elif biomarker == 'wild_type':
            explicitWaitVisibility(detailedVariantType)
            self.typeDetailedVariantType(detailedVariantType, biomarker)
            if world.variantdata[biomarker]['detailed_variant_type'] == 'wild type fusion':
                self.typeGeneFieldPartner(geneFieldPartnerWild, biomarker)
            self.typeGeneField(geneField, biomarker)
            self.typeDetailedVariantType(detailedVariantType, biomarker)

        elif biomarker == 'MSI':
            self.typeDetailedTypeOfMicrosatelliteInstability(detailedTypeOfMicrosatelliteInstability, biomarker)

        elif biomarker == 'TMB':
            self.typeDetailedTypeOfMutationalBurden(detailedTypeOfTumorMutationalBurden, biomarker)

        self.typeComment(commentBox, biomarker)
        self.typeAssayType(assayType, biomarker)
        explicitWaitClickable(self.dashL.nextButton).click()

    def verifyVariantCreated(self):
        explicitWaitVisibility(self.cvL.verifierVariantCreated)
