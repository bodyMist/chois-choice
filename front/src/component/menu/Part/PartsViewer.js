export default function PartsViewer() {
  return (
    <div className="product_list_area">
      <div className="main_prodlist main_prodlist_list"> 
        <ul className="product_list">
          <li className="prod_item">
            <div className="prod_main_info">
              <div className="thumb_info">
                <div className="thumb_image imageEnlarge">
                  <a href="#" className="thumb_link">
                    <img src="/3600.jpg"/>
                  </a>
                </div>
              </div>
              <div className="main_info">
                <div className="head_info">
                  <strong className="pop_rank">
                    <span className="screen_out">인기순위</span>
                    1
                  </strong>
                  <a href="#" className="prod_name goodsLink">
                    <strong>AMD 라이젠5-3세대 3600 (마티스) (멀티팩(정품))</strong>
                  </a>
                </div>
                <dl className="prod_spec_set">
                  <dt className="screen_out">상세스펙</dt>
                  <dd>
                    <ul className="spec_list">
                      <li className="spec_item">AMD(소캣AM4)</li>
                      <li className="spec_item">3세대 (Zen 2)</li>
                      <li className="spec_item">7nm</li>
                      <li className="spec_item">6코어</li>
                      <li className="spec_item">12쓰레드</li>
                      <li className="spec_item">기본 클럭:3.66GHz</li>
                      <li className="spec_item">최대 클럭:4.26GHz</li>
                      <li className="spec_item">L3 캐시:32MB</li>
                      <li className="spec_item">TOP:65W</li>
                      <li className="spec_item">PCIe4.0</li>
                      <li className="spec_item">메모리 규격:DDR4</li>
                      <li className="spec_item">3200MHz</li>
                      <li className="spec_item">내장그래픽:미탑재</li>
                      <li className="spec_item">기술 지원:SenseMI,StoreMi</li>
                      <li className="spec_item spec_item_last">쿨러:Wraith Stealth 포함</li>
                    </ul>
                  </dd>
                </dl>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  );
}