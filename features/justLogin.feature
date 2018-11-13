Feature: Login screen for mhGuide Reporter Portal


  @LoginCase


  Scenario: Login, Search for a case
    Given I am logged in
    Then I go to the [Settings] tab
    When I go to the [Filters and rulesets] tab

    When I expand the details with org unit [OU-A] and labtest configuration [MH Autotest (unpaired)]
    Then I am in the [variant filter] tab
    When I change under [False positive filter] the value of [Variant detected in previous analysis] to [6]



#
#
#
#    Then I see the header [Org unit, Labtest configuration, Most recent change, Product]
#
#    When I expand for Orgunit [QA] the Labtest configuration [Agilent V5 (paired)]
#    Then I see the [Activate filters] toggle
#    And I see the [Variant filter] tab is activated
#    And I see the following subsections [SNV, Indel, CNA, Fusion] under the [Variant filter] tab
#    And I see the [SNV] tab is activated
#    When I enter for the field [Variant detected in previous analysis] the value is [10] under the section [False positive filter]
#    And I enter for the field [References to variant in COSMIC] the value is [10] under the section [False positive filter]
#    And I enter for the field [References to variant in COSMIC] the value is [10] under the section [False positive filter]
#    And I enter for the field [References to variant in COSMIC] the value is [10] under the section [False positive filter]
#    And I enter for the field [References to variant in COSMIC] the value is [10] under the section [False positive filter]
#    And I enter for the field [References to variant in COSMIC] the value is [10] under the section [False positive filter]
#
#    And I select the [Effective] checkbox
#    And I unselect the [Effective] checkbox
#
#    And I set the value [3.0] in [lower boundary] for the subsection [Variant allele frequency (VAF) filter]
#    And I set the value [3.0] in [upper boundary] for the subsection [Variant allele frequency (VAF) filter]
#
#    And I click on the [save all changes] butotn
#    Then I see a popup with the message[This will change the edited ruleset for all future cases. Click Yes to continue or No to cancel.]
#    When I click on [Yes]
#    Then  I see the message [Ruleset saved]

    #When I click on the [Variant filter] tab

        #When I expand the details with org unit [MTSINAI] and labtest configuration [XML import Complete (unpaired)]


    #When I search for the case [none] [new-SA071-paired-fastq]
    #When I click on the arrow for the case [new-SA071-paired-fastq]
    #Then Verify the [Case ID] [wrong] in the expanded list



   # When I search for the case [none] [new-SA071-paired-fastq]
    #When I click on the expand detail button
    #Then I see the case

    #When I click on the case [new-SA071-paired-fastq]
    #Then I am in the [Variant] tab
#    When I click on [Settings] button
#    Then I am in the global settings
#    When I click on [Filters & Rulesets] tab
#    Then I see the header [Org unit, Labtest configuration, Most recent change, Product]
#    When I expand for Orgunit [QA] the Labtest configuration [Agilent V5 (paired)]
#    Then I see the [Activate filters] toggle
#
#    #Then I see the header [Variant filter, Lineage and zygosity, CVI match quality, Biomarker detection, Prioritization settings, Labtest appendix] with tabs for filters
#    #Then I click on the [Ineffective & Toxic] tab
#    #Then I click on the [Prognostic & Diagnostic] tab
#    #Then I click on the [Report] tab







