select count(DISTINCT(wlan_fc_moredata)) from AWID_REMOVED_NULL where class='normal'
select count(DISTINCT(wlan_fc_moredata)) from AWID_REMOVED_NULL where class='arp'
select count(DISTINCT(wlan_fc_moredata)) from AWID_REMOVED_NULL where class='amok'
select count(DISTINCT(wlan_fc_moredata)) from AWID_REMOVED_NULL where class='authentication_request'
select count(DISTINCT(wlan_fc_moredata)) from AWID_REMOVED_NULL where class='deauthentication'

select wlan_fc_moredata from AWID_REMOVED_NULL where class='normal'