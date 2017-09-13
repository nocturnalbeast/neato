import os
import shutil
import neatoDeleter

print """neatoChromeCleaner started!"""

#Web Cache
#Delete the web cache, which reduces time to display revisited pages


"delete" search="glob" path="$localappdata\Google\Chrome\User Data\B*.tmp"/>
"delete" search="walk.all" path="$localappdata\Google\Chrome\User Data\Default\Application Cache\"/>
"delete" search="walk.all" path="$localappdata\Google\Chrome\User Data\Default\Pepper Data\Shockwave Flash\CacheWritableAdobeRoot\"/>
"delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\Cache\"/>
"delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\GPUCache\"/>
"delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\Media Cache\"/>
"json" search="file" path="$localappdata\Google\Chrome\User Data\Default\Preferences" address="dns_prefetching/host_referral_list"/>
"json" search="file" path="$localappdata\Google\Chrome\User Data\Default\Preferences" address="dns_prefetching/startup_list"/>
"json" search="file" path="$localappdata\Google\Chrome\User Data\Default\Preferences" address="net/http_server_properties/servers"/>
"json" search="file" path="$localappdata\Google\Chrome\User Data\Local State" address="HostReferralList"/>
"json" search="file" path="$localappdata\Google\Chrome\User Data\Local State" address="StartupDNSPrefetchList"/>

#Cookies
#Delete cookies, which contain information such as web site preferences, authentication, and tracking identification

check($localappdata\Google\Chrome\User Data\*\Cookies)
check($localappdata\Google\Chrome\User Data\*\Cookies-journal)
check($localappdata\Google\Chrome\User Data\*\Extension Cookies)
check($localappdata\Google\Chrome\User Data\*\Pepper Data\Shockwave Flash\WritableRoot\)

#DOM Storage
#Delete HTML5 cookies

    <action command="chrome.databases_db" search="file" path="$localappdata\Google\Chrome\User Data\Default\databases\Databases.db"/>
    <action command="delete" search="glob" path="$localappdata\Google\Chrome\User Data\Default\Local Storage\http*localstorage"/>
    <action command="delete" search="glob" path="$localappdata\Google\Chrome\User Data\Default\Local Storage\http*localstorage-journal"/>
    <action command="delete" search="walk.all" path="$localappdata\Google\Chrome\User Data\Default\databases\http*\"/>

    <label>Form history</label>
    <description>A history of forms entered in web sites</description>
    <action command="chrome.autofill" search="file" path="$localappdata\Google\Chrome\User Data\Default\Web Data"/>

    <label>History</label>
    <description>Delete the history which includes visited sites, downloads, and thumbnails</description>
    <!-- keep /History before /Favicons -->
    <action command="chrome.history" search="file" path="$localappdata\Google\Chrome\User Data\Default\History"/>
    <action command="chrome.favicons" search="file" path="$localappdata\Google\Chrome\User Data\Default\Favicons"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\chrome_shutdown_ms.txt"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Safe Browsing Cookies-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Archived History"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Archived History-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\History Provider Cache"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\History-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Network Action Predictor"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Network Action Predictor-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Origin Bound Certs-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\QuotaManager-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Shortcuts"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Shortcuts-journal"/>
    <action command="delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\Thumbnails"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Thumbnails"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Thumbnails-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Top Sites"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Top Sites-journal"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Visited Links"/>
    <action command="delete" search="glob" path="$localappdata\Google\Chrome\User Data\Default\History Index ????-??"/>
    <action command="delete" search="glob" path="$localappdata\Google\Chrome\User Data\Default\History Index ????-??-journal"/>
    <action command="delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\Session Storage\"/>
    <action command="delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\JumpListIcons\"/>
    <action command="delete" search="walk.files" path="$localappdata\Google\Chrome\User Data\Default\JumpListIconsOld\"/>

    <label>Passwords</label>
    <description>A database of usernames and passwords as well as a list of sites that should not store passwords</description>
    <warning>This option will delete your saved passwords.</warning>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Login Data"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Login Data-journal"/>

    <label>Search engines</label>
    <description translators="'Factory' means a search engine that is installed by default 'from the factory,' but this is different than a 'default search engine' https://lists.launchpad.net/launchpad-translators/msg00283.html">Reset the search engine usage history and delete non-factory search engines, some of which are added automatically</description>
    <action command="chrome.keywords" search="file" path="$localappdata\Google\Chrome\User Data\Default\Web Data"/>

    <label>Session</label>
    <description>Delete the current and last sessions</description>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Current Session"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Current Tabs"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Last Session"/>
    <action command="delete" search="file" path="$localappdata\Google\Chrome\User Data\Default\Last Tabs"/>

    <label>Vacuum</label>
    <description>Clean database fragmentation to reduce space and improve speed without removing any data</description>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Archived History"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Cookies"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Extension Cookies"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\History"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Plugin Data\Google Gears\localserver.db"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Plugin Data\Google Gears\permissions.db"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Thumbnails" type="f"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Top Sites"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\Web Data"/>
    <action command="sqlite.vacuum" search="file" path="$localappdata\Google\Chrome\User Data\Default\databases\Databases.db"/>
    <action command="sqlite.vacuum" search="glob" path="$localappdata\Google\Chrome\User Data\Default\History Index ????-??"/>
    <action command="sqlite.vacuum" search="glob" path="$localappdata\Google\Chrome\User Data\Default\databases\http*\?"/>