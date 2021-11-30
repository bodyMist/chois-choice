import { useState } from "react";
import OptionList from "./OptionList";
import inf from "../menulist.json";

export default function PartsSelector({getPartItems, getItemsByOption}) {
    const option = ['cpu', 'gpu', 'mainboard','memory','hdd', 'ssd', 'power', 'cooler', 'case']
    const [Selected, setSelected] = useState("1")
    const handleSelect=(e)=>{
        setSelected(e.target.value);
        getPartItems(option[e.target.value-1]);
    }

    const [checkedItems, setCheckedItems] = useState(new Set());
    const checkedItemHandler = (inf, isChecked) => {        
        if (isChecked) {
            checkedItems.add(inf);
            setCheckedItems(checkedItems);
            
        } else if(!isChecked && checkedItems.has(inf)) {
          checkedItems.delete(inf);
          setCheckedItems(checkedItems);
        }
        getItemsByOption(checkedItems)
    };
    return (
        <>
            <div className="dir_location">
                <ul className="dir_list">
                    <li className="dir_item dir_home">
                        <a className="dir_link">홈</a>
                    </li>
                    <li className="dir_item">
                        <label></label>
                        <select name="category1" title="카테고리 대분류">
                            <option>PC주요부품</option>
                            <option>PC저장장치</option>
                            <option>PC주변기기</option>
                        </select>
                    </li>
                    <li className="dir_item">
                        <label></label>
                        <select name="category2" title="카테고리 중분류" value={Selected} onChange={handleSelect}>
                            <option value>중분류 선택</option>
                            <option value="1">CPU</option>
                            <option value="3">메인보드</option>
                            <option value="4">메모리</option>
                            <option value="2">그래픽카드</option>
                            <option value="6">SSD</option>
                            <option value="5">HDD</option>
                            <option value="9">케이스</option>
                            <option value="7">파워</option>
                            <option value="8">쿨러/튜닝</option>
                        </select>
                    </li>
                </ul>
            </div>
            <div className="optional_nav optioan_total_show">
                <div className="nav_header">
                    <div className="head_info">
                        <h4 className="nav_title">옵션 검색</h4>
                    </div>
                </div>
                <div className="spec_list_wrap">
                    <div className="detail_list_wrap">
                        <div className="spec_list">
                            {inf.Parts[Selected-1].map((items)=>{
                                return (
                                <dl className="spec_item">
                                <dt className="item_dt">{items[0].title}</dt>
                                    <OptionList inf={items} checkedItemHandler={checkedItemHandler}/>
                                </dl>)
                                ;
                            })}
                        </div>
                    </div>
                    <div className="spec_price">
                        <dl className="spec_item">
                            <dt className="item_dt">가격</dt>
                            <dd className="item_dd">
                                <div className="prod_price_selector">
                                    <label>
                                        <input
                                            type="text"
                                            name="minPrice"
                                            className="price_input"
                                        />
                                    </label>
                                    &nbsp;원&nbsp;~&nbsp;
                                    <label>
                                        <input
                                            type="text"
                                            name="minPrice"
                                            className="price_input"
                                        />
                                    </label>
                                    &nbsp;원
                                    <button
                                        type="button"
                                        className="btn_search"
                                    >
                                        검색
                                    </button>
                                </div>
                            </dd>
                        </dl>
                    </div>
                </div>
            </div>
        </>
    );
}
