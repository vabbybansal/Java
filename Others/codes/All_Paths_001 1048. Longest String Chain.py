# Learning
# Greedy and Exploring all paths are esssentialy opposite to each other - We could see that even though the question talked about joining subsequent words with an inc of 1, we cant really think of a greedy appraoch here as the output could be created in multiple ways, and rather this was a problem with exploring all paths
# I also initially thought about creating duplicate nodes for each string if it has multiple parents, but then because it would have required a lot of duplication, could think of a way which reduces dupication - creating a Node class which stores and represents each string, but can be connected to multiple other nodes / strings without duplicating entities
# IMPORTANT LEARNING: (DON'T DUPLICATE) If an element is connected to multiple other elements and there is possible duplication possibility [of the entities and hence the work], then CREATE NODE STRUCTURE AND CONNECT IT TO OTHER NODES using pointers. Now, we will not have to duplicate entities as that is taken care of by the graph edges

# Two methodologies
# 1)
#   - sort the initial list of words
#   - start adding next big string to the current small string and keep track of the height and MAX while adding itself
# 2)
#   - to avoid doing the expensive sorting, we can
#   - simply join nodes like a graph unlike the above approach which comes up as a tree
#   - for each new node, we ll have to look at len-1 words as well as len+1 words unlike above which looked only at len-1
#   - once the graph is made (might be disjoint), run DFS on each node (prevent visiting twice by jabing a visiting marker, and return the max travelled)





# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.
#
#
#
# Example 1:
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
# Note:
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

class Node(object):

    def __init__(self, val):
        self.val = val
        self.len = len(val)
        self.next = []
        self.maxHeight = 1

class Solution(object):

    MAX = 0

    def checkPred(self, small, big):
        if len(small) >= len(big):
            return False

        smallP = 0
        bigP = 0

        # maximum violations possible == 1
        violations = 0

        while smallP < len(small) and bigP < len(big):
            if small[smallP] != big[bigP]:
                violations += 1
                smallP -= 1
            if violations > 1:
                return False
            smallP += 1
            bigP += 1
        return True

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Sort the list on length
        # words.sort(lambda x,y: cmp(len(x), len(y)))

        self.MAX = 0

        seed = Node("")
        seed.maxHeight = 0
        # list to store all the starter nodes
        # globals = [seed]
        # hash table to store all the nodes length wise for fast access
        hashTableLens = {}

        # iterate over each word
        for s in words:
            lenS = len(s)
            newNode = Node(s)
            FOUND_PARENT = False

            # add the new node in the hash table
            if lenS not in hashTableLens:
                hashTableLens[lenS] = []
            hashTableLens[lenS].append(newNode)

            # look for len-1 in table
            if lenS-1 in hashTableLens:

                # iterate over len-1 list
                lenMinusList = hashTableLens[lenS-1]
                for node in lenMinusList:
                    # check connection
                    if self.checkPred(node.val, newNode.val):
                        node.next.append(newNode)

            if lenS+1 in hashTableLens:

                # iterate over len-1 list
                lenPlusList = hashTableLens[lenS+1]
                for node in lenPlusList:
                    # check connection
                    if self.checkPred(newNode.val, node.val):
                        newNode.next.append(node)

        for key in hashTableLens:
            for node in hashTableLens[key]:
                self.DFS(node, 1)
        return self.MAX

    def DFS(self, node, h):

        if self.MAX < h:
            self.MAX = h

        # indicator for visited
        if node.maxHeight == "Visited":
            return

        node.maxHeight = "Visited"

        localMax = h
        for next in node.next:
            localMax = self.DFS(next, h+1)



    def longestStrChain_2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Sort the list on length
        words.sort(lambda x,y: cmp(len(x), len(y)))

        seed = Node("")
        seed.maxHeight = 0
        # list to store all the starter nodes
        globals = [seed]
        # hash table to store all the nodes length wise for fast access
        hashTableLens = {0:[seed]}
        MAX_HEIGHT = 0

        # iterate over each word
        for s in words:
            lenS = len(s)
            newNode = Node(s)
            FOUND_PARENT = False

            # add the new node in the hash table
            if lenS not in hashTableLens:
                hashTableLens[lenS] = []
            hashTableLens[lenS].append(newNode)

            # look for len-1 in table
            if lenS-1 in hashTableLens:

                # iterate over len-1 list
                lenMinusList = hashTableLens[lenS-1]
                for node in lenMinusList:
                    # check connection
                    if self.checkPred(node.val, newNode.val):
                        node.next.append(newNode)
                        newNode.maxHeight = max(newNode.maxHeight, node.maxHeight+1)
                        if newNode.maxHeight> MAX_HEIGHT:
                            MAX_HEIGHT = newNode.maxHeight
                        FOUND_PARENT = True
            if FOUND_PARENT == False:
                globals.append(newNode)
                if MAX_HEIGHT == 0:
                    MAX_HEIGHT = 1
        return MAX_HEIGHT


obj = Solution()
print obj.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
# print obj.longestStrChain_2(["bdca", "b","bca","ba","bda","xyz", "a"])
# print 10
# print obj.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
# print obj.longestStrChain_2(["xiktrzpllggpfhyz","xpvsadeteueapiix","zmorruxheofxuzex","bktrzyuehqwflufv","wqisffnotrirxbcp","aconyfdaykglfxav","pairidyzwwudqyta","sdzwiexpiyzgnhgc","lzlyojxrzptucbkf","ksarxkcvqlhxurlz","kjbarurxolakwihg","spsiggyyvgiuhphk","zezawnaquzluvuvn","emeqduevvcznedgp","owjtxugswkrxwzfz","cshycwyzsxvjhrbt","ynkncdozldfbqnfj","iwovhiehaccvatgz","dqhunbmsjpthcdfw","lgsnkmoqmxvfkiwa","momznchoxeidauve","yszsqqkkgbhmcywc","jmsxlhcbjmfcbyii","fpffixflnkkrbijp","nljoruhzvlbbgkar","mgvztbcaxiizxafw","fwyesmzklxikhucs","cvhqnzhvzqqugkzq","evlvkhkhvektaqzv","yoamimsgybrjiysh","puzqcdprgfoifrpk","wsabcyxsvguqjlwo","ynvplivbamsjhadj","vzclfnoyzwqgwdkn","hyplcmrdekcbbeyn","rppdgwoazxeprgfl","evfnvtptdrdpffzw","jsspmpfqglybfybg","eddmsykvjikawpay","lnwunpmynuaqvfol","pcyzxbevkkwqqzpp","ywfczslwhstbqfbr","htgpgymwsfxrnrye","nzqwprxcxsekojei","hbrcljojxswrhoyv","jqzveafebmxtyfss","ckdfgaolrhzxixnh","ivzcajsvoptxootv","qoqewvcuupgmkivu","shhlxmishdntfhlo","wjmkzlpalxmfzcgn","mepokparotrqnemv","vtsqliqsbmzbllgb","zmnkmggbhnxloaap","endivarwladtznjm","sembmqbmcrjyujcr","nbbfkdqbtlhaokaa","jwaxklstistompuy","phimhmzcsttecexa","epipamvsepcdtbiz","zgspvaobuqnexcwe","uvrvpfxyhtvzlicj","wlylymcdftakkkqa","oisjvrsmegjixnnb","jpnrprfzgbywheel","aziiguuaqbdahzjx","rygswbtmahxvhwbk","ahswzmqbaubxspac","nntlulwoozdaexyd","appbjriqggjsyzoe","xxxgwrsvieuegjkq","pnzubazuvvfnmqvk","niynekxdblbrkwpz","wqrptmyzblryrrrg","mvluaslaelyxckfq","nwhssmjrpilcxrmt","dlxclhgmntznfhcm","dftdsjboiafzvkkz","acadbdleuxfmbxqc","qaqpasmynpxfjdsw","hvwrunfcclbhevpj","yzvunptcshgotdlv","kgotgvctpyfxbcoh","lljzznkehauqewie","vffuplsorjjdthhp","zmreuskfdbprryaw","kviuixrytezksbot","kophvascdsbownac","jivnmjrizuwtazax","cyadbnavjljctafv","bemhrieubmxyuwfv","oddludjpryyfzbeq","wphjknashuwimbxf","npizyejuohihhzzt","dykbvtgfgeekrgoi","cmhjucdtgtwtiwas","rjqskbawrmnzshnt","ofywvslglhkaiumn","pvueaekdrnnprnky","ueryzfsugvvslvol","olbzohuhofshstpa","rgmosneefyykwylr","xuribzbmsltjopqo","ontfyozarnhgdstb","dyvccexekxphwcko","rsdvnxgjbpjcnnvh","dpnrtkqkxuwldacd","yncimflzgqqrzoqc","hgsaprfvnweeeewu","hdkzblepnxuyjhlf","jvvbgwlscpzizapl","vdffkheluhyojtnh","mermqeejjlafbmxd","uyvuvbqdytscnfyz","lrtbyxwxyddyaxtf","gedmrchbqgvkotmi","qlcowjpuvkfjqxum","oftdpsytaduihcxd","obajpmwhejqsblci","twssfmikespenbzr","wnnqzpfiiuwwfuuv","ukhdpagsnzqdmact","vwfyvxkjzhbupmlw","xngmdijsjvvtyvtq","rgubdakwbpkxioci","huplukfiojyacfkj","nsdmrjpqsdukdpew","smfkhpygclpurxqf","fxmbyktwczcgynkc","tfztrnpvdlfmkgbe","nkhojszihwhhquwa","tdbslimcyhqfvrok","vpzqjxdnhslpuflc","mdzvaomxztaxksdu","glnqtpmeorbiadte","gczbrhnfdqgajzgf","rwdkhzmbqzmvlwcs","mlntmvimjylsujlz","wmiefnldbraymkju","lpaviqjiycarwesn","zdqyqgutpbfxmpxn","qzltbkakofafidqd","cpahjjkgmibthjzf","dyoxushnollyftme","cyrhvyophhfyddjx","sbxrvfigixujebht","nvqoqxxrazujtyeh","paazqdfhkdwaqkmv","rjldzftqhtmylykc","kowftuamqixgfqmt","rxfesuqxnapimrmq","ytkpfytwwnydthmu","iyczlvslsithmkmw","lkhsvjtqxzkddrhk","zlbfpluogpujathk","dghnjblmsdwzezgy","hmklqpzpyqlvzive","llzigsbqpotjmjee","dtzckprahpkdelac","cuhpbxoxzqhicaph","xcwfocnwumvkmeqp","fgtnwsabjkmolrpc","hzcujbznyakrcpsm","aemewyoawdmwhfwk","hqmippezmqpcymuf","wymqfukkhawuxqiw","pjufiaqyvngbhbrn","qhwmkmsysiyikmff","wopvhgumesumbjxy","spiokgvbnilenzuw","yyudbokugnuncqoe","jnlybhmotnwqparz","usjnrlqwypjlzocr","ystpdsqmjylnnxvq","rxjjkqqytayovkaf","nfyocvpvbhqdfwss","xxcjwqtdqpvntoeg","dtqakeyreorapbrq","ioytgpelskuipmav","arebazhqaqewubpr","ojaljxttzhagaxcq","bbashltmuxjmzajl","msxqgbvyngfxuffz","sayhyhbttspffmea","dojhjxqysqjtpfba","zbduzbujxtzkviub","lksprbncaureecjh","mrngtsyoncuishfs","dqfnagsokobmfmoo","eqwcfzdvijsaqmlq","najyizvppgkpitdr","ondnlppfjzwdgxnj","ksqtbgzqivhpbfdc","ymfoipmguqszggvl","jdnfzajaaqumnxyj","hwzcimzuqscvnjfs","nkrdjkjwsmkqdsrb","jehdirdqvsdgamin","sdrlhblfhbdvgfyq","kvblhbikpiyfeyve","jbyamqdrqxvoyefa","wsmarkjrffzaieod","nspqxdgactlpvpqm","sfiyfkvkwhobjvdq","lfkdeuaktpifcjng","roagvbtztkgmkvqg","wlkdznewqkhkewdx","seiwzsfttlqfdadv","yuceesivscgmyrrc","ojtexjphdrhmsprz","wcucwofaizczofjs","klczhgljhzzsuvak","evuifhwdydndsxxt","hcdwpymrqjygylum","ryfusxexyfnilwom","epcupjuzvfjwuiad","buqotlgepgqftmmc","pdsnynulyfniyuzs","vvmyhsaxyvovbdqp","qqtqcffokvzgmlgo","hzewuqlucekopklg","toybrsyhzaujhdrc","efvruspjvsnmliro","yzoxwpspebhetqvv","rarfzsudtbmzoypu","aquyojszfkaokotd","fitbwlfqvhnwrtax","hvvscnwgceuznchj","zsmxhzbyhkpnswug","qfonmsqvdkudqaiq","nyaxjhptoarlmnky","tfibnnvdjrvycztd","vynuzqdnfzfmwaqf","zrpuaohviipjexed","zahuitenwcxymrad","sujmcuphqzesaipy","uznbydacfbxbeegk","ubbinzehagmzcogg","mrwojblmmbjtmfze","hqapxztodlfaljfy","wiamundsnczdyvjb","pbyclnvkyudkajfe","szkhlwkwyolxrrpy","jmwverfcekgvtkod","ejdtuncxjobpirwg","xqwfvkzisrsnwplr","tmaqyvgfkfhewcdx","xumoyodfmqrmnzmk","mgtpddcpyuzmlxpc","mmnocpibybafvwrq","kwizksnmhzeiqrns","vpawfsjjpfvjwbvg","lldygnmrkxhzescs","mbikmxubsrqxqbhu","jbxlnxuuvzjrrexf","emgybzkmqxmdchpf","kklcxkdckwzevmde","ozlmogdvnqepreck","jzygzibnyxuxdcsx","oklynnzxkqcgzpiu","lprxrfjzymfjqgwg","jmokfkaocybmjask","juptrygjxjzdeeub","ufstbspzhkrppprp","ighmbeckwdjrnoos","guvkcqtmmylmnyck","tizidkensluzgyvh","iwsofcdjxjfhngxs","jffseqvzsckhnrnn","hgoqoiawrwnlyngz","erxhpdltdssscuon","oiasxoyahyaxqatk","kefbwqepjggbvebx","qmmbzltxgdzylbbv","jctvfmwrbwzwtima","kcxspccwpuxivzit","cvmysypziuonbfgh","epsmrspexkznyrnj","vwquqjykfixtbyot","loxsdumstqhhpjif","sggvhefovvvpffpd","uljipogohwwivvbt","idxthvlxlspocoyd","imctxvlmvjbtyeyi","bgkotxifetnnacwm","tqykskbwquulvikt","cvjjfaxnnetixidp","xchygwwfqajkrwvp","zjukjirmyewadosy","cnwcnpwarvyfpwtp","dbtolrkvvlzxesai","jrlpuaomdcenttzm","ehqirdljbxdxmvxe","wxrmnixoxsteemmd","xitrbxrdacsotmtj","dlwmafzothymbuae","ygfksnszzcgglqur","lenkvahauisijaxs","xajlwcxsxzoiojsl","dwisrywksldxjxdi","bbbhsalznmefauho","jumkzqoyfyborsaj","inpsilobcuuxtgoi","mymrqhuvwisrmexk","grnjrmehiqlgcpbz","sgsaxezwlpgtiymk","mfslwhaphtprtaxc","zdxqhvndadhloqpz","ncjfkzimkwogclax","iqpaohyzfksttazm","rmoqdtymviqsjniz","rtkcymghagoaqqqg","dwhdbvcnbznacbjz","zoeswywxfgirujup","pfjsjvvrhcaxxwjs","ydrdgvrxgnnwpnjd","lfrrgamvzazpbitq","ijshitmmlsyyjmyc","tgvqkjwgrtuzxvll","alhpfpagcohodqvw","wtixmmpfzuiyzhsf","xqijnoiuvepnyqfs","qmnqohcoxusausjs","meaaacbykxmdbvkz","oxvjobihweqdysfd","dqsjyjymwweoixop","bipeqynjfbsbcsqr","zenwqxbazquebegu","qejxdoxhevoxemds","uswoispqfjbpydsb","ibsgttnszzqhtmwc","pnkryvxcagddabjf","wpegggnqckqguaae","shaqmjnduaqbnzxf","jonthlxvetudyfhg","mklelncpthmpcehu","vgeudpxslqrrijra","ihxttlctrwdufhez","iryczxurgxrzfajf","mcewoovlrvwijjem","nehqsfopdapxqlab","fbtyzlmqekwisbah","nqpqxehlcimpelha","tfqfsvbwhwrichjx","kzqscjcztadwjejl","jjijrbdlwbrjpwkw","vwcaayyzhwcfnnmx","zjkhsytflegwjkkp","dplwqojosauzafdm","oqfozatkblhrgtfi","glfmqehnombtfgbg","czabawvpcpydwoon","hvmznnpicdvdzdyy","kclyliwllsvibzlk","nftyancrxobdbfjx","alzjewkdbzxqcaix","yfancgrvzrnzmuzj","gpypzuibdddqbloy","xibvzvvnolzrvpyq","pitgmjtutfsnxnzq","czufnnhramkfpkbm","kzxwgwbahhdhuytx","hqwoltpnuhpcqzok","wumeihirikhbyikb","tfpjwcjfzyerzjfc","fbmmxuvqfvaykzsa","wtnnkjvzekgdhuff","xbwctjaxedowxems","ioaaspgjiofmoqbn","ohlhsvcdkzzuribl","guktsqvpryrdqzga","chemfkrzyqembfej","lcusyleynlmnppib","qvzoheeewlnqgble","qdcgdeowgfmbrqdg","htmaxzyvhhzgkmgj","chfmaakdcmdisblk","ghyyniziyomygcpb","euawkihcitbjgkft","bwnhzvhngqgtelxx","qqvzvipnpnxwjdmh","rnuqcolrntmmomsp","kbgdgqrtrdkyzosx","ixgsakrqjrkvfdlt","kjhrdhnvvyaxzetl","yrrojhxuwjyavgjk","cesdsugrjhpxsaii","xffsukdgcvilpqfh","ancdzbybotxcpzac","qjizmxkoqahnvxgg","hphxgaxdljcerorm","jzbdjctqsmfdigih","doaiyylxeuomnhdp","keolfwsgcseojukl","arjmppsyylqexsmw","brqkiottwhoiqcgd","hcxgdpswyylulrul","hzulljnybiokqepq","lpqyuzwbcbntdyee","qcmgkcgeqmincyyw","ogvrkvcxpffcpinj","oascdubsabtlvdmn","prcgsvfvszrssgie","uegcagrmffwcelmw","qtjjswzpiojupncy","lserouxcyqehosiq","jgltxtcpezgrtdgf","hjtatgbdvfesnaig","axrnrhprfqrwiktm","aogkespeqwukqert","larxhqesfuoyltgu","fpcqlckdutivwtkq","ybubxarenanvzjgr","woswqevbyhfpqiso","zfcrwwpiorpteufs","amifyqrslrdouixd","nmmibyijjcpelmqs","boflnieugsqmcnhv","enyowtrftynimjen","kdlufutmobarilwd","ztebyjzpmyjdbyrg","yyjxtlmuyqeitktq","oajufmkauerezlsr","mvukjpbipmqstfxn","kuqeiudhyiljpfpt","pryfblvlkyvpezsm","fidsjsfjufhpaphb","fzekfqsuwdtquedn","lkpnroglpgzzoybu","innbafxvbytlsigm","tmwtfujmmvjewdzh","rmfinvjrqhpsnxhd","doxujrxhzkzobwmj","cioucshndcoqztap","ovxjjipqjssxroxu","qviosuedrcewtjtl","fepzyaeszkydushx","afejocxcstudgaeq","gfjirksxxuzcptkg","gnwpcxzkuiygfuly","ouzqwnofqqkxszsp","klzvwgocpetqdugl","oqwyutucnbcaaxju","gugxzdgiiobrexha","xsucijhduodsjchk","hnelnardrbldrbud","plghaapqbfvvsdti","rzuuqwrxqcqiwacg","miulftkqwzmqwjoh","nrznnvhkemqgkgsv","mrkonrvwgoalymqk","jqmxyblxbzpxpkbj","rhqpahrhaeciwixb","dfcubemuxeusnavg","ysnbvnykgwjmhzsw","scxumdiofeylxoyv","ouhpzdchtugixgjv","rrtlphgzqpycvywu","cgotqwsaeupidlrv","jncamcnzcxlyyjxr","vsakgcymrtvrqscc","enbenlumtbciuury","oheynbmnigspazsp","lmkvfxtofexvtgwg","wlewrzzfxycmrbpx","vguwcdvwipuqazob","yksktdynhitagmpg","svzruilehenkvfia","pzlnrwmudphjslbn","jpummgetjasepymb","vxmfjkrzlohtdpwr","xguibwhpoexuohdx","qjunlphmxdoyiryg","zezoqukwfpunpvas","oqkjoxtimqpqgvhk","skvpwsiqndmioijf","feurthvdmgbrsdof","rhvyqdohbcrjyfgc","wfextoqgurlidolc","hrtghbpwclgckwul","sgevgruxaubafxxu","mblchtvvgkelrdgc","cujeayqrsobatezc","dvtnssdpbwiibwgk","segfwjurrpvypqhy","mdnlbkmktgartjsa","hrjblfvhwuwkaimf","yppjqpcynukdyxms","ggkggyjgnmjwnulw","bixyknzirpjtbsmh","nwoewhxwxqcyvbdk","apacykmfikgasfnt","qudntrnzpjjstlvd","aapyeicnnjayzpsx","hizvlnkcxlfdskzl","wbpdshkxbgrcrtuy","qyxrjwgdwafqyjja","shdxgkohqusmtxyj","guiibrenwlwdfqdu","zrnyjgjxhmfhrxnz","zuangeanwpbrlbfo","fdymwqknctlwfaba","dlkmklltaayemlft","yyysdolfabylsjrg","gmiibamodgytuiuf","isyoyymrhbrdjhpn","wrtfabspemlumtgx","dvjuwwfwmpiupgck","nebbtjvdnjalxhsl","tcxzbutpqofeylqz","tsdqdpnapokuseex","zwunfqyxzmxmrrsf","xzsifvaxkcszeizb","joxubjzwefssesgw","hiieivjqhnkcnyno","mohyaqoxpxinphhi","bkvflxhhrmvxhzdw","pbepdlkmtouummtw","anzvhlsofhioqgin","dquevxvzkkkqcinz","kekxlgvposiptxvj","gcbthdcmkrvuyzdl","hoknyusetkzotukx","yvmtlcslgqddbvss","wexlzaeiulovhpmg","tupzatgxfmvuhjpi","kaauifmbtjysfrll","llzqpjbkbweyzsrg","satcdfjqpdfxspin","nnwiyjnjevophnyr","wnunpxcdtirvhdox","uruituzetnmwhrnh","hcmiobabscioptog","mfdmmdgcmpmrdliw","deejoflzvlktixvm","ejtdbaqztpkdopss","ofoftpbqyzfvkonu","dunlzvfgjumynokk","egqszmsmriiwvjer","nofkywrqjcdvxxku","mvoyvtbpygmkbdcu","afianivkzwjnwkci","sgrejmqqgpqdjppg","brthsiugiznwdmdy","tlrojibptbanjitw","akokdarsnmottxmh","bzdgpcfeidqgkgbe","xvzpvrribefsxpql","rgxhimpyxkwcfsjv","cggayworxwjqyiub","cmgzthvdrylcpnbk","gsmxjnesizgcsekp","akwwjehnqfuyocyf","axhvzkohbfgmtwdy","mpyjkvfcswhgzvpk","pyyzavmxfbjrxkjp","dckouvaboaemzsen","ufoobfwtgglkiejr","ihhsucogdfyqsyxi","xtlqoakdccwftbwh","hqylfbwzshvmqosn","glnwsyqmlepquhkc","mczbursxycktfnuw","alahgczbaamdcqwj","tbwosedfdoqsvjtq","cbdcfyiahwipsecd","ducrktddpqxjzpxg","wklvpwvitdjsewvd","drzlmxkmpgdylokv","taqdfookiilzkiro","mdffhfhuybenkcev","yrymkwdusmnywllh","jcyimhirgojwaoxm","kafauauqkotoqjiy","xiialniocdyfzafz","owsrrupnnaydwtxl","xkeouczeqqlchlgc","hntwpcscciwsgygj","owpcumbgyvjvfhtd","ktlsodliwlzwcibg","nnldarmumhwycnmh","nuerkodfikshltex","tffseksbnlnxesio","rjbdhjvzugiktweq","gnzdvnbhygyghpwu","bnfrpvbjclzmywzs","kmwgvkdqpouwyess","arbewnglfhvtmvsb","qdolszesjymaplah","bxztrreifjcufeoh","mzwcodwpnsxnuuyq","wazfzajcncxdzfbj","rlanqzxkdmairfdc","sofxpdfcnliidmmk","hsqfijtkdtuaqgyo","kwnbgcdjiexvbzdn","wgsxamvqwwuifzix","jgbxyfsvbxzqxsgb","vuwfygtglcnvxzsk","honyknsswnjcptwb","icjauzxupjwwhwpj","vlovlanrqwcmlamd","krlwkpmwtntartvx","vsrtgppgbjjlxfrc","yieuhkezfjvfkpmv","ukaqifssnvwdjeoy","epclonsnnbarsqnd","ctysmruhtaoacsac","gnibyypurvnidiwt","qscakllhmgsbfpre","sbetrfmxghzkxrtp","vleowjsgbedgfmzq","erzilcxdivctcora","hyjhfxtlufkmwvgr","vraqzndefvdtxitm","pgyfnrfodtdqhmbp","xlkxpaeeozpjyrit","duleiczxmbsucghn","qqwwlhvfabfnusog","klxmgipnwcpokpnd","vlqmoqjlgzjmxmbg","lehcgamxsyimgqth","ikiqdgdazrlnuvhp","eyvaunsgpbvwzglq","kxljlaflhctkhwmo","froggfbsizuulkfx","ysojldfnjquxkuby","nubgsezgeaqgykuh","qtxehkitspyuiwgv","ggwwrtinpnhaiisd","bwdajoxpyhoccnqx","rzskcnwzcpdkblds","qyteswscuyowqppg","ebqhnhnuaghorrvk","cfmrramffdrutfzi","knzyqqufxnwsdrhu","poberjevqgkyjumv","ysmecwxntijlizbk","hlvfvpvjktmckjfd","vsloukblhjsnmgkq","iiakujirkwctpgdr","lpubmtozuxpjmwgf","kuewhaleowcaynxy","zjlqaifjrdfadgrl","tnzctlowmlgawrxm","qacfsvqhefepwiem","hmjubfyxupxpzdvg","xcqhjsomlbumwjtu","tpehxtytrlckjvlq","ngxutcbaefvyliqa","ftvfutqmnfzbjink","pgoeccaudnbsqscj","awwjurtrykdrjtbc","ynezhnnhonpuuzva","rgtqcghgvchoaogt","patrurplbggnwhlv","tjhzftdmeaiywmln","mreypefpylkgexpv","gksehpkxnwefkrco","jtvyzkruooxbjqfm","bpsgfhshuwkqxrwb","yvmntgnflmbktjlf","pmljczrbipccxjdi","qfnqzrrvbympedkv","akeupscuobqbcfqw","gnskawfxgrtuftdc","hauvfnycukkppdqd","bixufwlszzajqlzz","tmrjqbqwyuphyaie","fnhhbtzbbwbfhxko","mvkiaeceziuslmxt","ojrxkjfbsxlerjsl","zhgpnnshnsnqshwn","yuwogfvyssztuloq","irbffueunbwnzwtx","iyskpivuxakcbfhv","atbagdawcyzntljd","qmujlsftooaozbpn","qzrjavjstbuabwhi","jutwslhqcqrzeczc","vwrmhpwceqfxephu","zfnoqqppnhfmfhbv","wljgjvzdsiniavkg","btybpkhywlzkjykt","cejyxdptihlsktcb","vcyswfrlnhzmtaia","hmzhjhacjnllowxy","qpvjntisszalfntz","ykbdsaziuesycane","bljxpmilmubcfwqs","itrbplovomeuskzf","bqnkulgxmynpyxzd","leigzrqyfatimwec","ptqcirqrythumuwi","dptobuaagzwoituq","tphtvjbzxqxfzuka","ptvpuptkchbviezm","rnhxmifuogzemuup","ohoolneyupjuwqor","gjmqofdevpixojun","enpqftzcgdhwelkf","ciceygubpdhqfniy","apynsbnunnoxlfdq","nbwxqqumaexnykid","rntcwdpesdiykkez","gjpzwlskzbxetzww","xxrhuizgdzaxaoex","autxzglluesrnrwy","kdairicuvymwwoyr","zrutddzwctgbumzk","obkybawixnyuxzzt","amdjsfkdmifanznp","cnehljlsqpfzhozb","vkqcewwgphgqepgt","tvcdgxtgtlsupzmp","jwfmxvzyifmrivob","udlrkmhctvhisner","hqbrzvfjcjrhzvwk","cqvbcpzevrlfbnih","qkiyxmyfbhoconwz","ueeinaivkijmwxdi","rfojlquphhyepcif","ksyauyzhzvhmlvie","pnhgrezabtxbskvc","pptkzarzlpwbaitt","ddigohzcjjuxqyeg","jvrfhqydfvwzazed","erarrgzaumixgqni","qjyorxvtmpiqxpfx","hboztgknncqhzkjo","npzxloqhgqxlqhdg","rnsexjucgwcrggrw","ujimkhuqdzlocgbe","aovfwupcyxjgrluy","gizxxxcyrlgdgdgo","zlvngmkudkjtzobe","oxctscxhejhlzzyz","qmgomhclqrnlfhty","mdsznhefbtqhyzsl","flvbzwnmzmqluuzk","bbnncfvxhgptphbz","oomyoauhctekkmsn","tgenginnsfhiltun","pkqjqqwssefivxga","mfyknvlpozwtrtaz","ggousvzylejekzpg","nfaqstxgdizlanmh","vylsuuxqbohshpkt","acrhvqbhhugqtsze","tiwmevmkqhejrkuc","cflnrqkxqladfvyw","wjgaclkmxfexjesk","bpbkbmclnbcpijix","inrbjyahiyticikc","cjfqshgdotgannhp","cxzvhwnpkpghkmtl","ofkpswfmbbineefh","rvlmoaewtmempzgk","wkyrlimewvlnmuqu","guzfbrsiyiqzgrqo","phhtrsbnukxzkfet","lxcgvolbyulhihls","wfpyacjadzrcwkpd","wejorrxxzbzjmyth","lbadematolnxdzze","jklbupheqamxwwsy","pjvvudugzxnwipdx","dpwunokcrtdpjtyg","pvdurwfbwrqdsglw","kmsjczauiavoqykt","lizayqgnambdedtk","lwgfgdwfzgtvxqdu","afugcswefvebvqvr","lxdixbbynshjzjoh","gssaoznpbzupodrp","rznjfxsedejtzgpz","rtfamilihwujtmpo","vomszawakyieztbb","bclrpuyirnbxvaww","tqpdutueqrzugfzf","drwykkfyrtndcugd","wvtvatfysdxdgwiv","iavsfyhjuuchvemw","kmqrqxkypgrtwdzm","pbfkxoipenmhhpof","cadlonvebfoeromt","qyjxdkqbrvppappl","zfxsqunbovtxwmri","xopkbsnbtgohjjxa","ohdhkkmvblvvgytm","sifxuziiktmjibyr","kimebzazlyuolwjj","jmgfevlvmlojrtcs","cgqplojfqcuphmro","vtwdrnbhitlyfvnh","zwmzrizzwtzkdesq","phobtkxspwmlwxmx","engdobejtugfryco","qkzphzqvsdnylzvy","jcyhhsdurkndwcly","ydzhixgjawtaovoa","fwbezynpdfwvdhyj","rqvryysermyxdrcb","dkcdsmptftqyownb","ttddstlnsslzqibg","hzvqbnxdiswcstxn","gbfhljqomjrymgtg","uvovxphnyqpjdtxg","nthcaxfbjkoccgkc","bdbtscfsdtnhdrfv","jqpjqxqqqcxfzatk","umshzxnxjnqejraw","qxhrnqbrksjezdlt","bmknwtszowqdkyhc","pphohnzexssageht","telkyzynxqyngoke","sokkljbfnipodald","euteauvdosuynftk","jztabxhknbyipqps","hcdgldgjfuswpvay","cqzyvqyamporjavs","tziqowtnllljesfm","vpmmnpwitelbfwxm","bqhuxffqalfwmgbr","hfpzjxubcqqdzuqw","hleetncbghqsgqwa","rvlslwomfojdqyyd","yffmhaeplliuhjuj","gcvohjswjyztvohl","wrlkwvkqiiwldeyn","inlhxetlftfjouxk","tjyfczuzclettniu","jcmqpohakfjgrrax","akawchgqvqnfuyvq","sugnviybbsqzebtu","gzzzysjongrfoeen","azssjkgjbrfmvgsx","rmpqulwllffxsnfj","rgoyofrggblrmbyp","nwzvyngclzlfkgwf","kummjpbxqhdkeqyz","mswfdekujajvxafv","nefdpiscmbvjnlti","uyauwvsuhbtfojdd","kjamhqbvrrbjliho","kqaurcbbmyywuiab","kfbyzxxmwrdwthig","iohwqwbifvmkuyxj","vnskhfsawdnmdyyx","mkwfizqreudyhqmb","izityyuklaymdqmb","pozwltgwxanbocsn","hjwdicoltaglfmhl","ilbvkhpioihyujxy","yfdnkhzttwrytoww","pzdhrqsdbiwiomzg","jdwbvgeinblpockt","vcmknnxqbixynfrh","ntqcqkgcckixbikw","kojiapomujowmdrd","hiaopdrosfoqxacw","gvujlbdedvczwwgh","lxnxjtlfntbevzmz","rlddsiuqlrvvctiv","vecnhsmlxalbfcff","yfrcupjpvtwyhacz","uuzbzycrsizwplfo","hnwceunfkiimtyse","ysiiagivwwwhczin","mixkqqtituipkujn","jhosvnmikftikmyq","uosgnkbknjlsxdyc","qvuaxcipxlgopbmh","fqtpyoujxfsapksi","plekjstfgxhrddgv","cydxunbwuqyumhlh","lgkuhghruliwxkfi","jihfylbrwsvhkalp","jratkunajghtbxyq","vutuzmtzfqhekccb","qkfhhjsidlrgpotf","tznorhrnoghalsqr","qqbwsmaysjkwaaqe","mleluhndzztpnbfq","gbcgpyaiugevmwyw","zkkyvbpnvfbnsofq","krzwepruljnsqgpv","isvzdewwotrtuzlo","ffeonobupfyjexhw","xobwrewjuzswgiun","gjfrgmfubwwrewwx","igcfvwlrhwklfnah","fusoxhgcfviaefml","anwjityxvxtlusln","xbiztfwmkulmtark","ftfrrunusghhnyeq","wfqyagcrfxhlgves","skdirtgtnydandxo","jcskdfsfmkjotvqf","aqrcnpqcfzqhadgd","oiduysjqedcodqza","cmhwcbjujgaljvwt","dbgszrmgqbyvtkpq","gtqsaynvzarreuul","wsuvznrcdjlbmkxt","typfsxzpwbttjjox","hsnawuxmjwxmeyiq","zkxzbnsbpyqlfiwh","zkipqwlefcovmzmu","dddtqlxmbjzvrxiv","ajgusqbvgnrzygbt","horrensepxqpyryl","jkpeaktozibbaywl","jgyaveybwapjgwip","oughftbvlwyciahg","dlaequtgwkihyhvb","qdiffxfpiugqnoos","jbahtlawzestkyth","roxqeyfgjlsrnicd","hcbxyfpeubhodred","ufyjgasabxtkfhnc","vcxigxzxycxeovpz","cokurkkegebaqwfx","mdmsbchaavotddkm","foepivugdhcmnkgr","orzagckhrrfgsnpo","pxnbttptnqdtmzie","wrjizbkckmvofbgs","voqefcisvdfcbytp","vwtrcxvauqxcrksi","siagsweegmiykqen","izrhqjbninpwarmr","xivrzppxxweltsvg","hvcebfnapiaksfca","govczulyzvsfsmpj","dzhwmcrdgjkmvuvx","zaksfepynunjbmqq","iehrvggqbvaeapjh","kanuzjwpopcqgbak","bhaeheazjxcqglqm","iqmpdwcfuuyosgyn","qiauizabgkibyxzj","scofrygvxnqsqbea","bpcvvblowfgifwie","xfmnehxkizrlnsqf","pwlvotcmaorvlcwp","bmudhqrbxbvtwkya","kxvirkeqxdtkwvwx","avgvcivemxpohcmk","ylzmhhrpdmuoswie","kvtjzksmqrxwpwzg","ecwjsgoplxtacjzc","wfgkozseluftpfed","rllaqpeibhztvlfa","ohqdtpgeepkpihjb","cvvvoenyssxxqrdh","kzxiwhzrqrdyqwmz","ykpdovivwjmtrnpf","nkkqpgvejmayvgsz","ijlhlwrfdhawiovi","nxuhoboamzjxobia","ckleiknfrzkdhjzm","dxdznhkrinlvvhxx","bizxqckimejfulej","arfcjgkqarvsoxkd","rdnnuqlevjphqgzz","rofxqvltumknbymj","qzwhhmjhksypxrrv","tuoyuhnypnqnyadt","shzzgvdudwjazhew","rnalnzrfwvgtdlfm","afrkxpqlnehkeqdw","qtrsuorzelbnbrze","khnnqybdnpfxsply","bvrmxeaeamhxhqzs","fjxctyzmlatnmqoz","lonxqpxrfgkstnfd","zfyybvfwwxprvbdt","ymjnseyckdyjtviv","xapsigwznlqgnikf","djdjzlmkwqqmlowd","fqkcngawjuuwiutx","hpyaasplrcdzthdj","vevzbfamiaiatucg","peoblkupcnaptzio","hootfkxumcixaeak","nzdldcltzlxiwyor","fzimqlyhahdrgalp","mhqddrvfttatcjbs","gvcysxobgwswdixh","zoaiwxniwjjhinpa","orgrfgndwodijuna","fzdezinzowvylrll","kblfmbbbnzvkequi","rzvzyhjfllfsnvco","afphivobxylgntff","nvuglcddusrwqlrv","lteldiqxzxwsnqfw","lhvsxfkktlktdvpg","xijltanucofgplbj"])
# print obj.checkPred("bat","abat")

