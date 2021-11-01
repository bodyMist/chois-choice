import { useState } from "react";
import Item from "./Item";
import inf from "../menulist.json";

export default function PartsSelector({getPartItem, list}) {
    const [Selected, setSelected] = useState("1")
    const getValue = (e) => {
        const value = e.target.value;
        getPartItem(value);
    }
    const handleSelect=(e)=>{
        setSelected(e.target.value);
        getValue(e);
    }
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
                            <dl className="spec_item">
                                <dt className="item_dt">제조사</dt>
                                <dd className="item_dd">
                                    <ul className="item_list item_list_popular">
                                        <li className="sub_item">
                                            <label title="인텔">
                                                <input
                                                    type="checkbox"
                                                    name="makerCode[]"
                                                    title="인텔"
                                                />
                                                &nbsp;인텔
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="AMD">
                                                <input
                                                    type="checkbox"
                                                    name="makerCode[]"
                                                    title="AMD"
                                                />
                                                &nbsp;AMD
                                            </label>
                                        </li>
                                    </ul>
                                </dd>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">인텔 CPU종류</dt>
                                <Item inf={inf.generation_intel} />
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">AMD CPU종류</dt>
                                <Item inf={inf.generation_amd} />
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">소켓 구분</dt>
                                <Item inf={inf.socket}/>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">제조 공정</dt>
                                <Item inf={inf.thickness}/>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">코어 수</dt>
                                <Item inf={inf.core}/>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">쓰레드 수</dt>
                                <Item inf={inf.thread}/>
                            </dl>
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
