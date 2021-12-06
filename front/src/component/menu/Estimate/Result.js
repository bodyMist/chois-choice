import { useState } from "react";

export default function Result({ list }) {
  const [selected, setSelected] = useState([{"selected":1}, {"selected":0}]);
  const changeSpec = (e) => {
    const id = e.target.id;
    let select = [{"selected":0},{"selected":0}];
    select[id-1].selected = 1;
    setSelected([...select]);
  }
    return (
        <div className="spec_box">
            <div className="show_box">
                <div className="show-least" onClick={changeSpec} id="1">최소사양</div>
                <div className="show-recommand" onClick={changeSpec} id="2">권장사양</div>
            </div>
            <div
                className={
                    (selected[1].selected == 1 ? "Selected" : "") + " least"
                }
            >
                <ul>
                    <li>CPU : {list[0].name}</li>
                    <li>RAM : {list[2].name}</li>
                    <li>GPU : {list[1].name}</li>
                    <li>Mainboard : {list[3].name}</li>
                    <li>HDD : {list[4].name}</li>
                    <li>SSD : {list[5].name}</li>
                    <li>POWER : {list[6].name}</li>
                    <li>CASE : {list[7].name}</li>
                </ul>
            </div>
            <div className={
                    (selected[0].selected == 1 ? "Selected" : "") + " recommand"
                }>
                <ul>
                    <li>CPU : {list[8].name}</li>
                    <li>RAM : {list[10].name}</li>
                    <li>GPU : {list[9].name}</li>
                    <li>Mainboard : {list[11].name}</li>
                    <li>HDD : {list[12].name}</li>
                    <li>SSD : {list[13].name}</li>
                    <li>POWER : {list[14].name}</li>
                    <li>CASE : {list[15].name}</li>
                </ul>
            </div>
        </div>
    );
}
