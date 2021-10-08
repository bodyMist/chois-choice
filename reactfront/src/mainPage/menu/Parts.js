export default function Parts() {
    return (
        <div className="prodlist_wrap">
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
                        <select name="category2" title="카테고리 중분류">
                            <option value>중분류 선택</option>
                            <option value>CPU</option>
                            <option value>메인보드</option>
                            <option value>메모리</option>
                            <option value>그래픽카드</option>
                            <option value>SSD</option>
                            <option value>HDD</option>
                            <option value>케이스</option>
                            <option value>파워</option>
                            <option value>쿨러/튜닝</option>
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
                                <dd className="item_dd">
                                    <ul className="item_list item_list_popular">
                                        <li className="sub_item">
                                            <label title="코어i9-11세대">
                                                <input
                                                    type="checkbox"
                                                    title="코어i9-11세대"
                                                />
                                                &nbsp;코어i9-11세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="코어i7-11세대">
                                                <input
                                                    type="checkbox"
                                                    title="코어i7-11세대"
                                                />
                                                &nbsp;코어i7-11세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="코어i5-11세대">
                                                <input
                                                    type="checkbox"
                                                    title="코어i5-11세대"
                                                />
                                                &nbsp;코어i5-11세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="코어i9-10세대">
                                                <input
                                                    type="checkbox"
                                                    title="코어i9-10세대"
                                                />
                                                &nbsp;코어i9-10세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="코어i7-10세대">
                                                <input
                                                    type="checkbox"
                                                    title="코어i7-10세대"
                                                />
                                                &nbsp;코어i7-10세대&nbsp;
                                            </label>
                                        </li>
                                    </ul>
                                    <div className="spec_opt_view">
                                        <button
                                            type="button"
                                            className="btn_spec_view btn_view_more"
                                        >
                                            <strong>nn</strong>개
                                        </button>
                                    </div>
                                </dd>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">AMD CPU종류</dt>
                                <dd className="item_dd">
                                    <ul class="item_list item_list_popular">
                                        <li className="sub_item">
                                            <label title="라이젠9-4세대">
                                                <input
                                                    type="checkbox"
                                                    title="라이젠9-4세대"
                                                />
                                                &nbsp;라이젠9-4세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="라이젠7-4세대">
                                                <input
                                                    type="checkbox"
                                                    title="라이젠9-4세대"
                                                />
                                                &nbsp;라이젠9-4세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="라이젠5-4세대">
                                                <input
                                                    type="checkbox"
                                                    title="라이젠9-4세대"
                                                />
                                                &nbsp;라이젠9-4세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="라이젠9-3세대">
                                                <input
                                                    type="checkbox"
                                                    title="라이젠9-3세대"
                                                />
                                                &nbsp;라이젠9-3세대&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="라이젠7-4세대">
                                                <input
                                                    type="checkbox"
                                                    title="라이젠7-4세대"
                                                />
                                                &nbsp;라이젠7-4세대&nbsp;
                                            </label>
                                        </li>
                                    </ul>
                                    <div className="spec_opt_view">
                                        <button
                                            type="button"
                                            className="btn_spec_view btn_view_more"
                                        >
                                            <strong>nn</strong>개
                                        </button>
                                    </div>
                                </dd>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">소켓 구분</dt>
                                <dd className="item_dd">
                                    <ul className="item_list item_list_popular">
                                        <li className="sub_item">
                                            <label title="인텔(소켓1200)">
                                                <input
                                                    type="checkbox"
                                                    title="인텔(소켓1200)"
                                                />
                                                &nbsp;인텔(소켓1200)&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="인텔(소켓1151v2)">
                                                <input
                                                    type="checkbox"
                                                    title="인텔(소켓1151v2)"
                                                />
                                                &nbsp;인텔(소켓1151v2)&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="인텔(소켓2066)">
                                                <input
                                                    type="checkbox"
                                                    title="인텔(소켓2066)"
                                                />
                                                &nbsp;인텔(소켓2066)&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="AMD(소캣AM4)">
                                                <input
                                                    type="checkbox"
                                                    title="AMD(소캣AM4)"
                                                />
                                                &nbsp;AMD(소캣AM4)&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="AMD(소캣TR4)">
                                                <input
                                                    type="checkbox"
                                                    title="AMD(소캣TR4)"
                                                />
                                                &nbsp;AMD(소캣TR4)&nbsp;
                                            </label>
                                        </li>
                                    </ul>
                                    <div className="spec_opt_view">
                                        <button
                                            type="button"
                                            className="btn_spec_view btn_view_more"
                                        >
                                            <strong>nn</strong>개
                                        </button>
                                    </div>
                                </dd>
                            </dl>
                            <dl className="spec_item">
                                <dt className="item_dt">제조 공정</dt>
                                <dd class="item_dd">
                                    <ul className="item_list item_list_popular">
                                        <li className="sub_item">
                                            <label title="7nm">
                                                <input
                                                    type="checkbox"
                                                    title="7nm"
                                                />
                                                &nbsp;7nm&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="10nm">
                                                <input
                                                    type="checkbox"
                                                    title="10nm"
                                                />
                                                &nbsp;10nm&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="12nm">
                                                <input
                                                    type="checkbox"
                                                    title="12nm"
                                                />
                                                &nbsp;12nm&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="14nm">
                                                <input
                                                    type="checkbox"
                                                    title="14nm"
                                                />
                                                &nbsp;14nm&nbsp;
                                            </label>
                                        </li>
                                        <li className="sub_item">
                                            <label title="22nm">
                                                <input
                                                    type="checkbox"
                                                    title="22nm"
                                                />
                                                &nbsp;22nm&nbsp;
                                            </label>
                                        </li>
                                    </ul>
                                    <div className="spec_opt_view">
                                        <button
                                            type="button"
                                            className="btn_spec_view btn_view_more"
                                        >
                                            <strong>nn</strong>개
                                        </button>
                                    </div>
                                </dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
