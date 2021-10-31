import axios from "axios";
import { useState } from "react";

export default function PartSelected(props) {
    const getPartName = (e) => {
        const id = e.target.id;
        props.getPartInf(id);
    }
    return (
        <div className="col-12 col-sm-8 MainSufferArear">
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CpuStuff" id="1" onClick={getPartName}>
                    CPU : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor MainBoardStuff" id="3" onClick={getPartName}>
                    메인보드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor RamStuff" id="4" onClick={getPartName}>
                    램 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor VgaStuff" id="2" onClick={getPartName}> 
                    그래픽카드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CpuCoolerStuff" id="8" onClick={getPartName}> 
                    CPU쿨러 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor SsdStuff" id="6" onClick={getPartName}>
                    SSD : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor PowerStuff" id="7" onClick={getPartName}>
                    파워 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CaseStuff" id="9" onClick={getPartName}>
                    케이스 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor HddStuff" id="5" onClick={getPartName}>
                    HDD : 미선택
                </div>
            </div>
        </div>
    );
}
