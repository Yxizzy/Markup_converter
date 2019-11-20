import QtQuick 2.12
import QtQuick.Controls 2.12
import QtWebEngine 1.0
ApplicationWindow {
id: window
visible: true
width:640
height:480
WebEngineView {
id: webEngineView
anchors.fill: parent
}Component.onCompleted: {
var html="<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01 Transitional//EN'>
<html><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head><body>

    <div bgcolor='#48486c'>
<input type='text' />
        <table width='720' border='0' cellspacing='0' cellpadding='0' align='center' background='http://title.jpg' height='130'>

            <tr height='129'>

                <td width='719' height='129'/>

                <td width='1' height='129'/>

            </tr>

            <tr height='1'>

                <td width='720' height='1'/>

                <td width='1' height='1'/>

            </tr>

        </table>

        <table width='720' border='0' cellspacing='0' cellpadding='0' align='center' height='203'>

            <tr height='20'>

                <td width='719' height='20'/>

                <td width='1' height='20'/>

            </tr>

            <tr height='69'>

                <td width='719' height='69' valign='top' align='left'>

                    <table width='719' border='1' cellspacing='2' cellpadding='0'>

                        <tr>

                            <td bgcolor='a5fdf8' width='390'><b>Stream Name</b></td>

                            <td bgcolor='a5fdf8' width='61'><b>Status</b></td>

                            <td bgcolor='a5fdf8' width='61'><b>Duration</b></td>

                            <td bgcolor='a5fdf8' width='185'><b>Start</b></td>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='390'>c:\streams\ours\Sony_AVCHD_<wbr>Test_Discs_60Hz_00001.m2ts</wbr></td>

                            <td width='61'><font color='#D0D0D0'>----</font></td>

                            <td width='61'>00:00:02</td>

                            <td width='185'>2010/06/15-15:06:17</td>

                        </tr>

                    </table>

                </td>

                <td width='1' height='69'/>

            </tr>

            <tr height='113'>

                <td width='720' height='113' colspan='2' valign='top' align='left'>

                    <table width='721' border='1' cellspacing='2' cellpadding='0'>

                        <tr bgcolor='a5fdf8'>

                            <td width='299'><b>Test Category</b></td>

                            <td width='61'><b>Error</b></td>

                            <td width='62'><b>Warning</b></td>

                            <td width='275'><b>Details</b></td>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#099eac'>All Tests (Sony_AVCHD_Test_Discs_60Hz_<wbr>00001.m2ts)</wbr></font></td>

                            <td width='61'><font color='#ff0000'>34787</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#800000'>  ETSI TR-101-290 Tests</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#800000'>  ISO/IEC Transport Stream Tests</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#800000'>  System Data T-STD Tests</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#099eac'>  Prog(1)</font></td>

                            <td width='61'><font color='#ff0000'>34787</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#099eac'>    VES(0xe0)</font></td>

                            <td width='61'><font color='#ff0000'>34787</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#1010F0'>      H.264/AVC Conformance</font></td>

                            <td width='61'><font color='#ff0000'>34718</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'>

                                <a><font color='#ff0000'>Sony_AVCHD_Test_Discs_60Hz_<wbr>00001.m2ts_Prog(1)_PID(0x1011)<wbr>_H264_Conf.txt</wbr></wbr></font></a><br/>

                            </td>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        Sequence</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        Picture</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        Slice</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        Macroblock</font></td>

                            <td width='61'><font color='#ff0000'>34718</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        Block</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#1010F0'>      HRD Tests</font></td>

                            <td width='61'><font color='#ff0000'>69</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'>

                                <a><font color='#ff0000'>Sony_AVCHD_Test_Discs_60Hz_<wbr>00001.m2ts_Prog(1)_PID(0x1011)<wbr>_H264_HRD.txt</wbr></wbr></font></a><br/>

                            </td>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#101010'>        HRD level</font></td>

                            <td width='61'><font color='#ff0000'>69</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#800000'>      Video T-STD Tests</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#099eac'>    AES(0xfd)</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='61'><font color='#000000'>0</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#808080'>      Audio Level Tests</font></td>

                            <td width='61'><font color='#808080'>Disabled</font></td>

                            <td width='61'><font color='#808080'>Disabled</font></td>

                            <td width='275'/>

                        </tr>

                        <tr bgcolor='white'>

                            <td width='299'><font color='#800000'>      Audio T-STD Tests</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='61'><font color='#800000'>No Lic</font></td>

                            <td width='275'/>

                        </tr>

                    </table>

                </td>

            </tr>

            <tr height='1'>

                <td width='719' height='1'/>

                <td width='1' height='1'/>

            </tr>

        </table>

    </div>



</body></html>"
webEngineView.loadHtml(html)
}
}