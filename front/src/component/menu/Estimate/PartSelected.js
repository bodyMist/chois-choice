import axios from "axios";
import { useState } from "react";

export default function PartSelected() {
    const [list, setList] = useState("");
    const loadPartList = (e) => {
        const id = e.target.id;
        console.log(`/api?${id}`);
        axios
        .get(`/api?${id}`)
        .then(({data})=>{
            setList({
                setList: data.Item
            })
        })
        .catch(e => {
            console.error(e);
        })
    }
    return (
        <div className="col-12 col-sm-8 MainSufferArear">
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CpuStuff" id="cpu" onClick={loadPartList}>
                    CPU : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor MainBoardStuff" id="mainboard" onClick={loadPartList}>
                    메인보드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor RamStuff" id="ram" onClick={loadPartList}>
                    램 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor VgaStuff" id="vga" onClick={loadPartList}> 
                    그래픽카드 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CpuCoolerStuff" id="cooler" onClick={loadPartList}> 
                    CPU쿨러 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor SsdStuff" id="ssd" onClick={loadPartList}>
                    SSD : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor PowerStuff" id="power" onClick={loadPartList}>
                    파워 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor CaseStuff" id="case" onClick={loadPartList}>
                    케이스 : 미선택
                </div>
            </div>
            <div className="col-xs-12 WillSelect StuffOnePart">
                <div className="col-10 col-md-5 text-left StuffInfor HddStuff" id="hdd" onClick={loadPartList}>
                    HDD : 미선택
                </div>
            </div>
        </div>
    );
}
