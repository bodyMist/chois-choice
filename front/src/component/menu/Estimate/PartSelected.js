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
                <div className="col-10 col-md-5 text-left StuffInfor CpuStuff" id="cpu" onClick={getPartName}>
                    CPU : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor MainBoardStuff" id="mainboard" onClick={getPartName}>
                    메인보드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor RamStuff" id="ram" onClick={getPartName}>
                    램 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor VgaStuff" id="vga" onClick={getPartName}> 
                    그래픽카드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CpuCoolerStuff" id="cooler" onClick={getPartName}> 
                    CPU쿨러 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor SsdStuff" id="ssd" onClick={getPartName}>
                    SSD : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor PowerStuff" id="power" onClick={getPartName}>
                    파워 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CaseStuff" id="case" onClick={getPartName}>
                    케이스 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor HddStuff" id="hdd" onClick={getPartName}>
                    HDD : 미선택
                </div>
            </div>
        </div>
    );
}
