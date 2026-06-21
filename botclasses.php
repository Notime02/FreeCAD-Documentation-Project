<?php
# ... (truncated) ...
            } else {
                return false;
            }
        }
    }

    /**
     * Gets up to nine recent edits to a page by a specified editor. Used to prevent bots from edit warring.
     * @param $page The wikipedia page to fetch.
     * @param $editor The editor's edits to fetch (usually the bot's user ID).
     * @return int The number of recent edits the user has made to the page (up to 9). "Recent edits" are edits made in the past day (24 hours).
     **/
    function recent_page_edits ($page,$editor) {
        $ds = 86400;    #number of seconds in a day
        $timestamp = date(DATE_ISO8601, time() - $ds);
        #echo $timestamp . "\n";
        $x = $this->query('?action=query&format=json&prop=revisions&rvslots=main&titles='.urlencode($page).'&rvuser='.urlencode($editor).
            '&rvend='.urlencode($timestamp).'&rvlimit=9&rvprop=user|timestamp|comment');
        #print_r($x);
        foreach ($x['query']['pages'] as $ret) {
            #print_r($ret);
            if (isset($ret['revisions'])) {
                #print_r($ret['revisions']);
                return count($ret['revisions']);
            } else {
                return 0;
            }
        }
    }

    /**
     * Gets the ten latest edits to a page. Used to find history that blocks page-movers from moving.
     * @param $page The wikipedia page to fetch.
     * @return int The number of page-edits found (up to 10).
     **/
    function ten_latest_edits ($page) {
        $x = $this->query('?action=query&format=json&prop=revisions&rvslots=main&titles='.urlencode($page).'&rvlimit=10&rvprop=user|timestamp|comment');
        #print_r($x);
        foreach ($x['query']['pages'] as $ret) {
            #print_r($ret);
# ... (truncated) ...
