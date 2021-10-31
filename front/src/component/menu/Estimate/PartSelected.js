import { useState } from "react";
import data from "../menulist.json";
export default function PartSelected({getPartInf, sList}) {
    // console.log(sList[0].name);
    const getPartName = (e) => {
        const id = e.target.id;
        getPartInf(id);
    }
    return (
        <div className="MainSufferArear">
            {
                data.class.map((classData, index) => (
                    <div className="WillSelect StuffOnePart">
                        <div className="text StuffInfor" id={classData.id} onClick={getPartName}>
                            {classData.name} : 
                        </div>
                    </div>
                ))
            }
        </div>
    );
}
