comp = app.project.items.addComp("3DEComp",3840,2160,1.000000000000000,3.583333333333333,24.000000000000000);
rootNode = comp.layers.addNull();
rootNode.threeDLayer = true;
rootNode.position.setValue([1920.000000000000000,1080.000000000000000,0.000000000000000]);
cam = comp.layers.addCamera("VFX_19",[0,0]);
camParent = comp.layers.addNull();
camParent.threeDLayer = true;
camParent.name = "camera_parent_VFX_19";
cam.name = "VFX_19";
cam.orientation.setValue([0,0,0]);
cam.autoOrient = AutoOrientType.NO_AUTO_ORIENT;
cam.parent = camParent;
cam.position.setValue([0,0,0]);
cam.position.setValue([0,0,0]);
idx = camParent.position.addKey(0.000000000000000);
camParent.position.setValueAtKey(idx,[1922.432216486587777,1077.738180935953551,3.730349284634066]);
idx = camParent.orientation.addKey(0.000000000000000);
camParent.orientation.setValueAtKey(idx,[0.599676261785080,17.416701177000093,-0.179500425188627]);
idx = cam.zoom.addKey(0.000000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.041666666666667);
camParent.position.setValueAtKey(idx,[1922.435742923896669,1077.738461507676902,3.733299586773465]);
idx = camParent.orientation.addKey(0.041666666666667);
camParent.orientation.setValueAtKey(idx,[0.604790477906988,17.222831054922366,-0.179077684087809]);
idx = cam.zoom.addKey(0.041666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.083333333333333);
camParent.position.setValueAtKey(idx,[1922.439266501916109,1077.738742882112774,3.736247591127697]);
idx = camParent.orientation.addKey(0.083333333333333);
camParent.orientation.setValueAtKey(idx,[0.633200162070887,17.009537970434813,-0.185237506593920]);
idx = cam.zoom.addKey(0.083333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.125000000000000);
camParent.position.setValueAtKey(idx,[1922.442784172772917,1077.739025788889876,3.739190179905283]);
idx = camParent.orientation.addKey(0.125000000000000);
camParent.orientation.setValueAtKey(idx,[0.656639913260401,16.809396524515886,-0.189900523273373]);
idx = cam.zoom.addKey(0.125000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.166666666666667);
camParent.position.setValueAtKey(idx,[1922.446292540758122,1077.739310819429420,3.742122701503190]);
idx = camParent.orientation.addKey(0.166666666666667);
camParent.orientation.setValueAtKey(idx,[0.677209375134767,16.610506844066599,-0.193598126429669]);
idx = cam.zoom.addKey(0.166666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.208333333333333);
camParent.position.setValueAtKey(idx,[1922.449787757946297,1077.739598376822414,3.745038456234041]);
idx = camParent.orientation.addKey(0.208333333333333);
camParent.orientation.setValueAtKey(idx,[0.698952544483001,16.408380391518183,-0.197450363833492]);
idx = cam.zoom.addKey(0.208333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.250000000000000);
camParent.position.setValueAtKey(idx,[1922.453265493186336,1077.739888646029158,3.747928450937545]);
idx = camParent.orientation.addKey(0.250000000000000);
camParent.orientation.setValueAtKey(idx,[0.717053525981521,16.198785990557042,-0.200046597579561]);
idx = cam.zoom.addKey(0.250000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.291666666666667);
camParent.position.setValueAtKey(idx,[1922.456720983644800,1077.740181587437064,3.750781459974037]);
idx = camParent.orientation.addKey(0.291666666666667);
camParent.orientation.setValueAtKey(idx,[0.748579916596728,15.982681581794148,-0.206129915947195]);
idx = cam.zoom.addKey(0.291666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.333333333333333);
camParent.position.setValueAtKey(idx,[1922.460149167769487,1077.740476954244741,3.753584394568921]);
idx = camParent.orientation.addKey(0.333333333333333);
camParent.orientation.setValueAtKey(idx,[0.759761545438746,15.764723264733227,-0.206429120593395]);
idx = cam.zoom.addKey(0.333333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.375000000000000);
camParent.position.setValueAtKey(idx,[1922.463544888593105,1077.740774331608691,3.756322947785683]);
idx = camParent.orientation.addKey(0.375000000000000);
camParent.orientation.setValueAtKey(idx,[0.790656717124580,15.552922316393433,-0.212009961046604]);
idx = cam.zoom.addKey(0.375000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.416666666666667);
camParent.position.setValueAtKey(idx,[1922.466903147960693,1077.741073193303009,3.758982452712861]);
idx = camParent.orientation.addKey(0.416666666666667);
camParent.orientation.setValueAtKey(idx,[0.818499007740171,15.322832344965464,-0.216308110598888]);
idx = cam.zoom.addKey(0.416666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.458333333333333);
camParent.position.setValueAtKey(idx,[1922.470219386505732,1077.741372970018801,3.761548869995229]);
idx = camParent.orientation.addKey(0.458333333333333);
camParent.orientation.setValueAtKey(idx,[0.841377146930519,15.120747794151415,-0.219491387309337]);
idx = cam.zoom.addKey(0.458333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.500000000000000);
camParent.position.setValueAtKey(idx,[1922.473489761578094,1077.741673122519614,3.764009809553376]);
idx = camParent.orientation.addKey(0.500000000000000);
camParent.orientation.setValueAtKey(idx,[0.852304159020055,14.900945519190348,-0.219184039374012]);
idx = cam.zoom.addKey(0.500000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.541666666666667);
camParent.position.setValueAtKey(idx,[1922.476711395928533,1077.741973212724361,3.766355490697086]);
idx = camParent.orientation.addKey(0.541666666666667);
camParent.orientation.setValueAtKey(idx,[0.872507000013549,14.687994823992819,-0.221244748451378]);
idx = cam.zoom.addKey(0.541666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.583333333333333);
camParent.position.setValueAtKey(idx,[1922.479882573487430,1077.742272966335804,3.768579553962119]);
idx = camParent.orientation.addKey(0.583333333333333);
camParent.orientation.setValueAtKey(idx,[0.899698461729261,14.492111909544564,-0.225163931291406]);
idx = cam.zoom.addKey(0.583333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.625000000000000);
camParent.position.setValueAtKey(idx,[1922.483002864347327,1077.742572321760463,3.770679654927253]);
idx = camParent.orientation.addKey(0.625000000000000);
camParent.orientation.setValueAtKey(idx,[0.932697714153641,14.273743238140725,-0.229980289163100]);
idx = cam.zoom.addKey(0.625000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.666666666666667);
camParent.position.setValueAtKey(idx,[1922.486073168265420,1077.742871461572349,3.772657792376106]);
idx = camParent.orientation.addKey(0.666666666666667);
camParent.orientation.setValueAtKey(idx,[0.947386848220222,14.053107416051965,-0.230065302690173]);
idx = cam.zoom.addKey(0.666666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.708333333333333);
camParent.position.setValueAtKey(idx,[1922.489095673666952,1077.743170824469416,3.774520347619545]);
idx = camParent.orientation.addKey(0.708333333333333);
camParent.orientation.setValueAtKey(idx,[0.967040330679547,13.837886288017723,-0.231313119776552]);
idx = cam.zoom.addKey(0.708333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.750000000000000);
camParent.position.setValueAtKey(idx,[1922.492073736457087,1077.743471097357542,3.776277835945392]);
idx = camParent.orientation.addKey(0.750000000000000);
camParent.orientation.setValueAtKey(idx,[0.987798014218959,13.633611147388033,-0.232857881147302]);
idx = cam.zoom.addKey(0.750000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.791666666666667);
camParent.position.setValueAtKey(idx,[1922.495011689218700,1077.743773188727573,3.777944392862759]);
idx = camParent.orientation.addKey(0.791666666666667);
camParent.orientation.setValueAtKey(idx,[1.014571937630041,13.423949023293552,-0.235560728200759]);
idx = cam.zoom.addKey(0.791666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.833333333333333);
camParent.position.setValueAtKey(idx,[1922.497914596133796,1077.744078185744684,3.779537035568512]);
idx = camParent.orientation.addKey(0.833333333333333);
camParent.orientation.setValueAtKey(idx,[1.039881167875441,13.217440002585171,-0.237790665080656]);
idx = cam.zoom.addKey(0.833333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.875000000000000);
camParent.position.setValueAtKey(idx,[1922.500787972004673,1077.744387298411311,3.781074753081191]);
idx = camParent.orientation.addKey(0.875000000000000);
camParent.orientation.setValueAtKey(idx,[1.073898095307249,13.012275900758254,-0.241825576879720]);
idx = cam.zoom.addKey(0.875000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.916666666666667);
camParent.position.setValueAtKey(idx,[1922.503637485033778,1077.744701794767934,3.782577486566450]);
idx = camParent.orientation.addKey(0.916666666666667);
camParent.orientation.setValueAtKey(idx,[1.096506313484153,12.806367067217701,-0.243076365593308]);
idx = cam.zoom.addKey(0.916666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(0.958333333333333);
camParent.position.setValueAtKey(idx,[1922.506468662708130,1077.745022931403810,3.784065064773790]);
idx = camParent.orientation.addKey(0.958333333333333);
camParent.orientation.setValueAtKey(idx,[1.104987915811344,12.586042198595640,-0.240811374274226]);
idx = cam.zoom.addKey(0.958333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.000000000000000);
camParent.position.setValueAtKey(idx,[1922.509286618502756,1077.745351883602780,3.785556158749379]);
idx = camParent.orientation.addKey(1.000000000000000);
camParent.orientation.setValueAtKey(idx,[1.132867716036862,12.366595444267066,-0.242651773262993]);
idx = cam.zoom.addKey(1.000000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.041666666666667);
camParent.position.setValueAtKey(idx,[1922.512095814440727,1077.745689679301677,3.787067315734579]);
idx = camParent.orientation.addKey(1.041666666666667);
camParent.orientation.setValueAtKey(idx,[1.146581455025772,12.163200723343131,-0.241612082027019]);
idx = cam.zoom.addKey(1.041666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.083333333333333);
camParent.position.setValueAtKey(idx,[1922.514899871209536,1077.746037140724638,3.788612125058827]);
idx = camParent.orientation.addKey(1.083333333333333);
camParent.orientation.setValueAtKey(idx,[1.173413983352869,11.963019056816607,-0.243258166733142]);
idx = cam.zoom.addKey(1.083333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.125000000000000);
camParent.position.setValueAtKey(idx,[1922.517701433765524,1077.746394837115758,3.790200559489265]);
idx = camParent.orientation.addKey(1.125000000000000);
camParent.orientation.setValueAtKey(idx,[1.182004139266372,11.747896436327325,-0.240695636989389]);
idx = cam.zoom.addKey(1.125000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.166666666666667);
camParent.position.setValueAtKey(idx,[1922.520502096503151,1077.746763051414291,3.791838524447065]);
idx = camParent.orientation.addKey(1.166666666666667);
camParent.orientation.setValueAtKey(idx,[1.211987711623927,11.540241852917170,-0.242500303768235]);
idx = cam.zoom.addKey(1.166666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.208333333333333);
camParent.position.setValueAtKey(idx,[1922.523302388286993,1077.747141763025411,3.793527635247156]);
idx = camParent.orientation.addKey(1.208333333333333);
camParent.orientation.setValueAtKey(idx,[1.230050246455762,11.324322133125682,-0.241571299831450]);
idx = cam.zoom.addKey(1.208333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.250000000000000);
camParent.position.setValueAtKey(idx,[1922.526101814183676,1077.747530647991880,3.795265229577368]);
idx = camParent.orientation.addKey(1.250000000000000);
camParent.orientation.setValueAtKey(idx,[1.248695571394757,11.111833581022927,-0.240691089316995]);
idx = cam.zoom.addKey(1.250000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.291666666666667);
camParent.position.setValueAtKey(idx,[1922.528898947708285,1077.747929096917005,3.797044609360339]);
idx = camParent.orientation.addKey(1.291666666666667);
camParent.orientation.setValueAtKey(idx,[1.251690346053001,10.930592588999053,-0.237381585368708]);
idx = cam.zoom.addKey(1.291666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.333333333333333);
camParent.position.setValueAtKey(idx,[1922.531691564976200,1077.748336249907197,3.798855493547906]);
idx = camParent.orientation.addKey(1.333333333333333);
camParent.orientation.setValueAtKey(idx,[1.285854230761274,10.722585327622072,-0.239277022109945]);
idx = cam.zoom.addKey(1.333333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.375000000000000);
camParent.position.setValueAtKey(idx,[1922.534476810389151,1077.748751046678308,3.800684651933866]);
idx = camParent.orientation.addKey(1.375000000000000);
camParent.orientation.setValueAtKey(idx,[1.298916716556145,10.508191318788283,-0.236930599647687]);
idx = cam.zoom.addKey(1.375000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.416666666666667);
camParent.position.setValueAtKey(idx,[1922.537251382457498,1077.749172288858972,3.802516680386536]);
idx = camParent.orientation.addKey(1.416666666666667);
camParent.orientation.setValueAtKey(idx,[1.326735041915131,10.277023288544351,-0.236740640498464]);
idx = cam.zoom.addKey(1.416666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.458333333333333);
camParent.position.setValueAtKey(idx,[1922.540011728075115,1077.749598710535793,3.804334870586689]);
idx = camParent.orientation.addKey(1.458333333333333);
camParent.orientation.setValueAtKey(idx,[1.328362003619860,10.097336211162848,-0.232930147083987]);
idx = cam.zoom.addKey(1.458333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.500000000000000);
camParent.position.setValueAtKey(idx,[1922.542754233988489,1077.750029052332820,3.806122122874698]);
idx = camParent.orientation.addKey(1.500000000000000);
camParent.orientation.setValueAtKey(idx,[1.336457204583612,9.900594148180781,-0.229829988451232]);
idx = cam.zoom.addKey(1.500000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.541666666666667);
camParent.position.setValueAtKey(idx,[1922.545475405250272,1077.750462133894189,3.807861849451081]);
idx = camParent.orientation.addKey(1.541666666666667);
camParent.orientation.setValueAtKey(idx,[1.341745961793853,9.701947399026675,-0.226155064687391]);
idx = cam.zoom.addKey(1.541666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.583333333333333);
camParent.position.setValueAtKey(idx,[1922.548172022018207,1077.750896919635807,3.809538817011023]);
idx = camParent.orientation.addKey(1.583333333333333);
camParent.orientation.setValueAtKey(idx,[1.353041076538297,9.482996710916325,-0.222960476642456]);
idx = cam.zoom.addKey(1.583333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.625000000000000);
camParent.position.setValueAtKey(idx,[1922.550841267997839,1077.751332573081754,3.811139882776809]);
idx = camParent.orientation.addKey(1.625000000000000);
camParent.orientation.setValueAtKey(idx,[1.351372863252298,9.315809376506657,-0.218794497001399]);
idx = cam.zoom.addKey(1.625000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.666666666666667);
camParent.position.setValueAtKey(idx,[1922.553480825978113,1077.751768495984834,3.812654585464182]);
idx = camParent.orientation.addKey(1.666666666666667);
camParent.orientation.setValueAtKey(idx,[1.371969646531748,9.099285744586009,-0.217011620653953]);
idx = cam.zoom.addKey(1.666666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.708333333333333);
camParent.position.setValueAtKey(idx,[1922.556088938120183,1077.752204349691283,3.814075562448739]);
idx = camParent.orientation.addKey(1.708333333333333);
camParent.orientation.setValueAtKey(idx,[1.375798016481919,8.904747592344524,-0.213002828115216]);
idx = cam.zoom.addKey(1.708333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.750000000000000);
camParent.position.setValueAtKey(idx,[1922.558664430787530,1077.752640057717372,3.815398775631369]);
idx = camParent.orientation.addKey(1.750000000000000);
camParent.orientation.setValueAtKey(idx,[1.391321706939185,8.701348508513821,-0.210525266439459]);
idx = cam.zoom.addKey(1.750000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.791666666666667);
camParent.position.setValueAtKey(idx,[1922.561206705644054,1077.753075790101320,3.816623540511357]);
idx = camParent.orientation.addKey(1.791666666666667);
camParent.orientation.setValueAtKey(idx,[1.397435385312809,8.461668346714459,-0.205669321378390]);
idx = cam.zoom.addKey(1.791666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.833333333333333);
camParent.position.setValueAtKey(idx,[1922.563715700398689,1077.753511931623279,3.817752365014360]);
idx = camParent.orientation.addKey(1.833333333333333);
camParent.orientation.setValueAtKey(idx,[1.397367956526492,8.278698767803743,-0.201243722980136]);
idx = cam.zoom.addKey(1.833333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.875000000000000);
camParent.position.setValueAtKey(idx,[1922.566191823897952,1077.753949037261236,3.818790615963309]);
idx = camParent.orientation.addKey(1.875000000000000);
camParent.orientation.setValueAtKey(idx,[1.404300643518565,8.088449931715180,-0.197626213452973]);
idx = cam.zoom.addKey(1.875000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.916666666666667);
camParent.position.setValueAtKey(idx,[1922.568635871229390,1077.754387779162698,3.819746041051042]);
idx = camParent.orientation.addKey(1.916666666666667);
camParent.orientation.setValueAtKey(idx,[1.399654014425547,7.900878641701920,-0.192433627562833]);
idx = cam.zoom.addKey(1.916666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(1.958333333333333);
camParent.position.setValueAtKey(idx,[1922.571048925093919,1077.754828889862438,3.820628182183283]);
idx = camParent.orientation.addKey(1.958333333333333);
camParent.orientation.setValueAtKey(idx,[1.401522211685049,7.714689852618427,-0.188177556825857]);
idx = cam.zoom.addKey(1.958333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.000000000000000);
camParent.position.setValueAtKey(idx,[1922.573432249926555,1077.755273106436334,3.821447721625568]);
idx = camParent.orientation.addKey(2.000000000000000);
camParent.orientation.setValueAtKey(idx,[1.400497390496196,7.534810527986271,-0.183681116168401]);
idx = cam.zoom.addKey(2.000000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.041666666666667);
camParent.position.setValueAtKey(idx,[1922.575787185144918,1077.755721119806822,3.822215805155817]);
idx = camParent.orientation.addKey(2.041666666666667);
camParent.orientation.setValueAtKey(idx,[1.419286333560288,7.330299651064896,-0.181121957445672]);
idx = cam.zoom.addKey(2.041666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.083333333333333);
camParent.position.setValueAtKey(idx,[1922.578115043460912,1077.756173532562570,3.822943386204828]);
idx = camParent.orientation.addKey(2.083333333333333);
camParent.orientation.setValueAtKey(idx,[1.411327647001271,7.155676740159429,-0.175838042205129]);
idx = cam.zoom.addKey(2.083333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.125000000000000);
camParent.position.setValueAtKey(idx,[1922.580417019482866,1077.756630827572508,3.823640631758419]);
idx = camParent.orientation.addKey(2.125000000000000);
camParent.orientation.setValueAtKey(idx,[1.413747824240524,6.960229775807517,-0.171352745425614]);
idx = cam.zoom.addKey(2.125000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.166666666666667);
camParent.position.setValueAtKey(idx,[1922.582694112866648,1077.757093348473745,3.824316424808801]);
idx = camParent.orientation.addKey(2.166666666666667);
camParent.orientation.setValueAtKey(idx,[1.412382150259128,6.767700145108771,-0.166474263970486]);
idx = cam.zoom.addKey(2.166666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.208333333333333);
camParent.position.setValueAtKey(idx,[1922.584947069138252,1077.757561291973616,3.824977989813339]);
idx = camParent.orientation.addKey(2.208333333333333);
camParent.orientation.setValueAtKey(idx,[1.421726122824512,6.591557823949759,-0.163234115648084]);
idx = cam.zoom.addKey(2.208333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.250000000000000);
camParent.position.setValueAtKey(idx,[1922.587176340040514,1077.758034710891025,3.825630657591605]);
idx = camParent.orientation.addKey(2.250000000000000);
camParent.orientation.setValueAtKey(idx,[1.410001036532514,6.437969649686447,-0.158131375222475]);
idx = cam.zoom.addKey(2.250000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.291666666666667);
camParent.position.setValueAtKey(idx,[1922.589382063955782,1077.758513526108800,3.826277775183917]);
idx = camParent.orientation.addKey(2.291666666666667);
camParent.orientation.setValueAtKey(idx,[1.406665462966014,6.259606373384228,-0.153404170675388]);
idx = cam.zoom.addKey(2.291666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.333333333333333);
camParent.position.setValueAtKey(idx,[1922.591564065699231,1077.758997545129887,3.826920755327881]);
idx = camParent.orientation.addKey(2.333333333333333);
camParent.orientation.setValueAtKey(idx,[1.423819884222736,6.056105002894451,-0.150246808596955]);
idx = cam.zoom.addKey(2.333333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.375000000000000);
camParent.position.setValueAtKey(idx,[1922.593721873865434,1077.759486484749914,3.827559250318320]);
idx = camParent.orientation.addKey(2.375000000000000);
camParent.orientation.setValueAtKey(idx,[1.401849431881578,5.918311839464123,-0.144573855421676]);
idx = cam.zoom.addKey(2.375000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.416666666666667);
camParent.position.setValueAtKey(idx,[1922.595854752983314,1077.759979995443246,3.828191426943794]);
idx = camParent.orientation.addKey(2.416666666666667);
camParent.orientation.setValueAtKey(idx,[1.409078631971463,5.737619832545059,-0.140898042322256]);
idx = cam.zoom.addKey(2.416666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.458333333333333);
camParent.position.setValueAtKey(idx,[1922.597961747108229,1077.760477685361138,3.828814313592025]);
idx = camParent.orientation.addKey(2.458333333333333);
camParent.orientation.setValueAtKey(idx,[1.410158092230752,5.567980005483257,-0.136850355630034]);
idx = cam.zoom.addKey(2.458333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.500000000000000);
camParent.position.setValueAtKey(idx,[1922.600041731139527,1077.760979142288079,3.829424187866833]);
idx = camParent.orientation.addKey(2.500000000000000);
camParent.orientation.setValueAtKey(idx,[1.416167421621419,5.378485491539440,-0.132770509466824]);
idx = cam.zoom.addKey(2.500000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.541666666666667);
camParent.position.setValueAtKey(idx,[1922.602093466131691,1077.761483952429899,3.830016973222405]);
idx = camParent.orientation.addKey(2.541666666666667);
camParent.orientation.setValueAtKey(idx,[1.391070830072145,5.260929680297115,-0.127574333068404]);
idx = cam.zoom.addKey(2.541666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.583333333333333);
camParent.position.setValueAtKey(idx,[1922.604115655150281,1077.761991715432259,3.830588615937966]);
idx = camParent.orientation.addKey(2.583333333333333);
camParent.orientation.setValueAtKey(idx,[1.393346502428171,5.080637228963202,-0.123415680495662]);
idx = cam.zoom.addKey(2.583333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.625000000000000);
camParent.position.setValueAtKey(idx,[1922.606106996753851,1077.762502055509913,3.831135418691439]);
idx = camParent.orientation.addKey(2.625000000000000);
camParent.orientation.setValueAtKey(idx,[1.406978824323294,4.898198964219051,-0.120159714352717]);
idx = cam.zoom.addKey(2.625000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.666666666666667);
camParent.position.setValueAtKey(idx,[1922.608066233897489,1077.763014628950259,3.831654313314455]);
idx = camParent.orientation.addKey(2.666666666666667);
camParent.orientation.setValueAtKey(idx,[1.396793851639125,4.747188219223681,-0.115620432119716]);
idx = cam.zoom.addKey(2.666666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.708333333333333);
camParent.position.setValueAtKey(idx,[1922.609992196881876,1077.763529128513028,3.832143062207803]);
idx = camParent.orientation.addKey(2.708333333333333);
camParent.orientation.setValueAtKey(idx,[1.399524947430084,4.580958751116816,-0.111798873514043]);
idx = cam.zoom.addKey(2.708333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.750000000000000);
camParent.position.setValueAtKey(idx,[1922.611883839823804,1077.764045285387283,3.832600384581046]);
idx = camParent.orientation.addKey(2.750000000000000);
camParent.orientation.setValueAtKey(idx,[1.406978845920802,4.417293170967596,-0.108387109477019]);
idx = cam.zoom.addKey(2.750000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.791666666666667);
camParent.position.setValueAtKey(idx,[1922.613740270905282,1077.764562869377642,3.833026009502871]);
idx = camParent.orientation.addKey(2.791666666666667);
camParent.orientation.setValueAtKey(idx,[1.407150113371714,4.241873188974395,-0.104103545374374]);
idx = cam.zoom.addKey(2.791666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.833333333333333);
camParent.position.setValueAtKey(idx,[1922.615560777328255,1077.765081687906786,3.833420662270712]);
idx = camParent.orientation.addKey(2.833333333333333);
camParent.orientation.setValueAtKey(idx,[1.397103322987516,4.100718253859353,-0.099926490507510]);
idx = cam.zoom.addKey(2.833333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.875000000000000);
camParent.position.setValueAtKey(idx,[1922.617344846349397,1077.765601584264459,3.833785993637502]);
idx = camParent.orientation.addKey(2.875000000000000);
camParent.orientation.setValueAtKey(idx,[1.399149411819125,3.936423235637242,-0.096069928800388]);
idx = cam.zoom.addKey(2.875000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.916666666666667);
camParent.position.setValueAtKey(idx,[1922.619092184002284,1077.766122435353964,3.834124463018710]);
idx = camParent.orientation.addKey(2.916666666666667);
camParent.orientation.setValueAtKey(idx,[1.397580969542229,3.807687385121474,-0.092828572764372]);
idx = cam.zoom.addKey(2.916666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(2.958333333333333);
camParent.position.setValueAtKey(idx,[1922.620802733080154,1077.766644149003241,3.834439187187151]);
idx = camParent.orientation.addKey(2.958333333333333);
camParent.orientation.setValueAtKey(idx,[1.391220786866841,3.649027742496971,-0.088560891090924]);
idx = cam.zoom.addKey(2.958333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.000000000000000);
camParent.position.setValueAtKey(idx,[1922.622476691662314,1077.767166660768908,3.834733765510357]);
idx = camParent.orientation.addKey(3.000000000000000);
camParent.orientation.setValueAtKey(idx,[1.398426340321500,3.495290107206359,-0.085274015375102]);
idx = cam.zoom.addKey(3.000000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.041666666666667);
camParent.position.setValueAtKey(idx,[1922.624114532967042,1077.767689930088636,3.835012091894357]);
idx = camParent.orientation.addKey(3.041666666666667);
camParent.orientation.setValueAtKey(idx,[1.398251383204435,3.351061048689583,-0.081749154405471]);
idx = cam.zoom.addKey(3.041666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.083333333333333);
camParent.position.setValueAtKey(idx,[1922.625717026639450,1077.768213935635913,3.835278162619473]);
idx = camParent.orientation.addKey(3.083333333333333);
camParent.orientation.setValueAtKey(idx,[1.407507203488711,3.211388487530270,-0.078864312987211]);
idx = cam.zoom.addKey(3.083333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.125000000000000);
camParent.position.setValueAtKey(idx,[1922.627285260827875,1077.768738669812592,3.835535888428999]);
idx = camParent.orientation.addKey(3.125000000000000);
camParent.orientation.setValueAtKey(idx,[1.418388220167699,3.008411141672310,-0.074455808542387]);
idx = cam.zoom.addKey(3.125000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.166666666666667);
camParent.position.setValueAtKey(idx,[1922.628820663645456,1077.769264132449280,3.835788918656355]);
idx = camParent.orientation.addKey(3.166666666666667);
camParent.orientation.setValueAtKey(idx,[1.408995748421834,2.889336740343298,-0.071037629416112]);
idx = cam.zoom.addKey(3.166666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.208333333333333);
camParent.position.setValueAtKey(idx,[1922.630325021974159,1077.769790323963662,3.836040484801494]);
idx = camParent.orientation.addKey(3.208333333333333);
camParent.orientation.setValueAtKey(idx,[1.411892698820933,2.736091024050419,-0.067411228968410]);
idx = cam.zoom.addKey(3.208333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.250000000000000);
camParent.position.setValueAtKey(idx,[1922.631800495114703,1077.770317238392636,3.836293270628965]);
idx = camParent.orientation.addKey(3.250000000000000);
camParent.orientation.setValueAtKey(idx,[1.419684325191073,2.553677042523076,-0.063267408586991]);
idx = cam.zoom.addKey(3.250000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.291666666666667);
camParent.position.setValueAtKey(idx,[1922.633249620617562,1077.770844856854183,3.836549315332623]);
idx = camParent.orientation.addKey(3.291666666666667);
camParent.orientation.setValueAtKey(idx,[1.429088739318032,2.415124855393706,-0.060233410047889]);
idx = cam.zoom.addKey(3.291666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.333333333333333);
camParent.position.setValueAtKey(idx,[1922.634675309777776,1077.771373142064022,3.836809955371695]);
idx = camParent.orientation.addKey(3.333333333333333);
camParent.orientation.setValueAtKey(idx,[1.422230592839793,2.264052937302460,-0.056196595486792]);
idx = cam.zoom.addKey(3.333333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.375000000000000);
camParent.position.setValueAtKey(idx,[1922.636080830758829,1077.771902034508230,3.837075809069787]);
idx = camParent.orientation.addKey(3.375000000000000);
camParent.orientation.setValueAtKey(idx,[1.422736354116704,2.141419780643250,-0.053173058630246]);
idx = cam.zoom.addKey(3.375000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.416666666666667);
camParent.position.setValueAtKey(idx,[1922.637469778100240,1077.772431450754539,3.837346805931955]);
idx = camParent.orientation.addKey(3.416666666666667);
camParent.orientation.setValueAtKey(idx,[1.436533578418979,1.975608529480065,-0.049533485381129]);
idx = cam.zoom.addKey(3.416666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.458333333333333);
camParent.position.setValueAtKey(idx,[1922.638846028365151,1077.772961284180155,3.837622259957736]);
idx = camParent.orientation.addKey(3.458333333333333);
camParent.orientation.setValueAtKey(idx,[1.438690593108880,1.793898627113741,-0.045046692695608]);
idx = cam.zoom.addKey(3.458333333333333);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.500000000000000);
camParent.position.setValueAtKey(idx,[1922.640213682830108,1077.773491408132259,3.837900983220497]);
idx = camParent.orientation.addKey(3.500000000000000);
camParent.orientation.setValueAtKey(idx,[1.443986383487081,1.676352829589533,-0.042250885744549]);
idx = cam.zoom.addKey(3.500000000000000);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
idx = camParent.position.addKey(3.541666666666667);
camParent.position.setValueAtKey(idx,[1922.641576999239760,1077.774021681241720,3.838181432953671]);
idx = camParent.orientation.addKey(3.541666666666667);
camParent.orientation.setValueAtKey(idx,[1.453900050930218,1.534476169410357,-0.038941556997386]);
idx = cam.zoom.addKey(3.541666666666667);
cam.zoom.setValueAtKey(idx, 4446.770803280716791);
camParent.parent = rootNode;
item = comp.layers.addNull(3.583333333333333);
item.name = "p02";
item.threeDLayer = true;
item.position.setValue([1920.910946822742972,1079.221258551060600,11.831686000000001]);
item.parent = rootNode;
item = comp.layers.addNull(3.583333333333333);
item.name = "p03";
item.threeDLayer = true;
item.position.setValue([1922.575462539833779,1078.977061489974176,11.831685999999999]);
item.parent = rootNode;
item = comp.layers.addNull(3.583333333333333);
item.name = "p04";
item.threeDLayer = true;
item.position.setValue([1922.147485208319722,1078.039540882304664,11.628964117674329]);
item.parent = rootNode;
item = comp.layers.addNull(3.583333333333333);
item.name = "p05";
item.threeDLayer = true;
item.position.setValue([1924.085252535518521,1077.908879460600929,6.379944148630784]);
item.parent = rootNode;
item = comp.layers.addNull(3.583333333333333);
item.name = "p07";
item.threeDLayer = true;
item.position.setValue([1922.728494184734245,1077.823633330749544,3.472016568424850]);
item.parent = rootNode;
rootNode.position.setValue([1920.000000000000000,1080.000000000000000,-0.000000000000000]);
rootNode.orientation.setValue([-0.000000000000000,0.000000000000000,-0.000000000000000]);
rootNode.name = "Scene";