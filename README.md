## info:

this script migrates layer 4 policies from FMC (firepower management center) and creates warnings if it detects applications or countries.

___

## usage:

1. Generate a backup file in the FMC. 
    - open the FMC webUI
    - Select System > Tools > Backup/Restore.
    - Select policy and objects and click "Export" at the bottom of the page
    - this will export a .sfo file. Don't change the extension!

2. Download this script "fmc.py" and put it in the same folder as the .sfo file
3. Install Needed python libraries.
    >pip3 install javaobj-py3
4. Execute the script, this will generate the set commands
    >./fmc.py
___

## known issues:

1. Continents for geolocattion and applications are not migrated, a warning is thrown when detected. 
2. It doesn't migrate IPS, antivairue sor any deep insspection feature.

___

## Migration notes:

- Typically the firepower appliances are in vwire mode. There's no special configuration to allow tagged traffic in firepower so you might need to [allow tagged and untagged traffic in Palo Alto firewalls](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClqSCAS)
- By default the firepower appliances allow non-sync TCP traffic. Review if asymetric traffic is expected.
- To review the initial migration offline your customer can [export all the configuration in PDF](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/configuration/guide/fpmc-config-guide-v60/Working_with_Reports.html#ID-2250-000008dd) so this can help you fine tune your migration before scheduling a call to review it with the customer.
