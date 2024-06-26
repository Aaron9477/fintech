select product_type from product_base_info pbi 
where issue_company_type  in (19,20,21,22,23)
and cp_id = 7761748

-- 查看兑付情况 
select info.product_code ,info.full_name ,pnv.* from product_net_value pnv 
join product_base_info info 
on pnv.cp_id = info.cp_id 
where pnv.actual_net_value is not null


select info.product_code ,info.full_name ,pnv.* from product_product_ytm pnv 
join product_base_info info 
on pnv.cp_id = info.cp_id 
where pnv.actual_yield_record is not null
and pnv.invest_start_date >'2020-01-01'



where issue_company_name like '%理财%'


where actual_end_date >'2022-06-30'

select  * from product_open_net_cycle ponc 

-- 查看四季报
select info.full_name,issue_company_name,papt.* from product_assets_pos_type papt 
join  product_base_info info
on papt.cp_id = info.cp_id 
where papt.report_date ='2023-03-31'
and info.issue_company_type  in (19,20,21,22,23)

--  普益 bank_wealth_product 表 

SET @now_date:= '2022-12-31';


SET @type_now_date:= '2023-05-18';

select
	issue_company_name as CompanyName,
	parent_bank as ParentCompName,
	case
		when issue_company_type = 19 then '国有行全资理财子公司'
		when issue_company_type = 20 then '股份制行全资理财子公司'
		when issue_company_type = 21 then '城商行全资理财子公司'
		when issue_company_type = 22 then '农村金融机构全资理财子公司'
		when issue_company_type = 23 then '合资理财子公司'
		else '其它机构'
	end as ParentCompType,
	-- EstablishmentDate 
 info.cp_id as FinProCode,
	info.full_name as product_name,
	case
		when (info.sale_start_date > now()) then '预售期'
		when (info.sale_end_date >= now()) & (info.sale_start_date <= now()) then '募集期'
		when (coalesce(info.actual_end_date, info.invest_end_date , "") >= now()) & (info.invest_start_date <= now()) then '运行期'
		when (coalesce(info.actual_end_date, info.invest_end_date , "") < now()) then '已到期'
		else ''
	end as SecuState,
	sale_start_date as PopularizeStDate,
	case
		when (raise_way = 1 ) then '公募'
		when (raise_way = 2) then '私募'
	end as RaisingType,
	case
		when (open_type = 0 ) & (is_net_value = 1) then '封闭式净值型'
		when (open_type = 0 ) & (is_net_value = 0) then '封闭式非净值型'
		when (open_type in (1, 2, 6, 7, 8, 9, 10)) & (is_net_value = 1) then '开放式净值型'
		when (open_type in (1, 2, 6, 7, 8, 9, 10)) & (is_net_value = 0) then '开放式非净值型'
		else ''
	end as OperationType,
	case
		when (is_cash_manage = 1) then '现金管理类'
		when (product_type = 1) then '固定收益类'
		when (product_type = 2) then '权益类'
		when (product_type = 3) then '商品及金融衍生品类'
		when (product_type = 4) then '混合类'
		else ''
	end as InvestmentType,
	AssetData.report_date as EndDate,
	coalesce(AssetData.asset_scale * 10000, info.actual_raise_scale, "") as AssetValue,
	-- replace(SUBSTRING_INDEX(sub_cp_id, ',', 1), '总份额:', '') as main,
 case
		when sub_cp_id is null then '产品'
		when replace(SUBSTRING_INDEX(sub_cp_id, ',', 1), '总份额:', '') = info.cp_id then '母产品'
		else '子产品'
	end as ProductType,
	invest_start_date as product_establish_date,
	invest_currency,
	case
		when (invest_currency = 'CNY') then '人民币'
		when (invest_currency = 'USD') then '美元'
		when (invest_currency = 'HKD') then '港元'
		when (invest_currency = 'AUD' )then '美元'
		when (invest_currency = 'GBP' )then '英镑'
		when (invest_currency = 'EUR' )then '欧元'
		when (invest_currency = 'JPY' )then '日元'
		when (invest_currency = 'CHF' )then '瑞士法郎'
		when (invest_currency = 'CAD' )then '加拿大元'
		when (invest_currency = 'SGD' )then '新加坡元'
		when (invest_currency = 'CHF' )then '新加坡元'
		when (invest_currency = 'NZD' )then '新西兰元'
		when (invest_currency = 'SEK' )then '瑞典克朗'
		else ''
	end as CurrencyUnit,
	short_name as SecuAbbr,
	min_hold_term as MinInvestTerm,
	'日' as MinInvestTermUnit,
	case
		when (risk_level = 1) then '低'
		when (risk_level = 2) then '中低'
		when (risk_level = 3) then '中'
		when (risk_level = 4) then '中高'
		when (risk_level = 5) then '高'
	end as RiskLevel,
	benchmark as Benchmark,
	benchmark_high as BenchmarkMax,
	benchmark_low as BenchmarkMin,
	fee.manage_fee,
	fee.carry_fee,
	-- fee.num,
 coalesce(actual_end_date, invest_end_date, "") as MaturityDate,
	is_cash_manage as inv_type,
	info.product_code as RegistrationCode,
	is_structure as IfStructure,
	case
		when (invest_term = '无固定期限') then 999999
		when (invest_term is not null ) then invest_term
		else null
	end as InvestTerm,
	product_series,
	transfer_date,
	trustee_bank,
	case 
		when (profit_type = 1) then '保证收益型'
		when (profit_type = 2) then '保本浮动收益型'
		when (profit_type = 3) then '非保本浮动收益型'
	end as profit_type,
	case 
		when(info.classify_type =1) then '总份额'
		when(info.classify_type =2) then '子份额'
		else '不区分'
	end as classify_type,
	info.customer_type as IssueObject,
	case 
		when (info.open_type = 0) then '封闭式'
		when (info.open_type = 1) then '定活两便型'
		when (info.open_type = 2) then '每日开放型'
		when (info.open_type = 6) then '客户周期型'
		when (info.open_type = 7) then '定开型(申赎同期)'
		when (info.open_type = 8) then '定开型(申赎不同期)'
		when (info.open_type = 9) then '最小持有期型'
		when (info.open_type = 10) then '其他半开型'
	end as open_type,
	info.open_rules,
	info.fixed_income_upper,
	info.fixed_income_lower,
	info.equity_upper,
	info.equity_lower,
	info.derivatives_upper,
	info.derivatives_lower,
	info.invest_strategy,
	info.top_raise_scale,
	info.actual_raise_scale,
	info.is_index ,
	info.is_early_redeem,
	info.old_invest_scope,
	product_type_table.report_date,
	product_type_table.product_type_son,
	product_type_table.asset_type,
	product_type_table.resource, 
	info.benchmark
from
	product_base_info info
left join (
	select
		t.cp_id, t.full_name, t.product_code , t.report_date, 
		coalesce(t.direct_scale ,t.actual_scale, "") as asset_scale
	from
		(
		select
			A.cp_id, A.full_name, A.product_code,
			asset.report_date, asset.actual_scale, 
			asset.direct_scale
		from
			product_base_info A
		left join (select * from(
		select *, rank() over(partition by cp_id
		order by
			report_date desc )rank_num
		from
			(select * from product_assets_pos_type
			where report_date <= @now_date)) tmp
	where
		tmp.rank_num = 1) asset on
			A.cp_id = asset.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23)
			and asset.primary_type = 99)t) AssetData on
	info.cp_id = AssetData.cp_id
left join (
	select
		t.cp_id, avg(t.fixed_manage_fee_rate) as manage_fee , avg(t.variable_manage_fee_rate) as carry_fee, count(*) as num
	from
		(
		select
			info.full_name, info.product_code , fee.*
		from
			product_fee_rate fee
		join product_base_info info on
			fee.cp_id = info.cp_id
		where
			info.issue_company_type in (19, 20, 21, 22, 23)
			and fee.fee_end_date >= @type_now_date
			and fee.fee_start_date <= @type_now_date) t
	group by
		t.cp_id) fee on
	info.cp_id = fee.cp_id
left join (
select
		t.* 
	from
		(
		select
			A.cp_id, A.full_name, A.product_code, dy.report_date,
			case 
				when dy.product_type_son =1 then '纯固收'
				when dy.product_type_son =2 then '固收+'
				when dy.product_type_son =3 then '偏股混合'
				when dy.product_type_son =4 then '偏债混合'
			end as product_type_son,
			dy.asset_type,
			case 
				when dy.resource = 1 then '事前'
				when dy.resource = 2 then '事后'
			end as resource
		from
			product_base_info A
		left join (
			select * from (
				select * ,rank() over (partition by cp_id order by report_date desc) rank_num 
				from (
				select * from product_sub_type_dynamic
				where report_date <= @type_now_date))tmp_dy
				where tmp_dy.rank_num = 1)dy on
			A.cp_id = dy.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23))t) product_type_table
		on  info.cp_id = product_type_table.cp_id
where
	info.issue_company_type in (19, 20, 21, 22, 23)

	
-- 费率 
select * from (
select cp_id,count(*) as num  from (
select *,rank()over(partition by cp_id order by fee_start_date desc ) rank_num from (
select info.full_name,info.product_code ,fee.* from product_fee_rate fee
join product_base_info info
on fee.cp_id = info.cp_id
where info.issue_company_type in (19, 20, 21, 22, 23)
and fee.fee_end_date > '2023-04-21' 
and fee.fee_start_date <= '2023-04-21')
)aa 
group by cp_id )
order by num desc 


select * from product_fee_rate fee 
where fee.cp_id = 7757403
and fee.fee_end_date > '2023-04-21' 
and fee.fee_start_date <= '2023-04-21'


-- 测试set 
SET @now_date:= '2022-02-27';
select * from product_net_value pnv  
where trade_date >= @now_date
	
-- 测试 info 
select top_raise_scale ,is_cash_manage ,raise_way ,actual_raise_scale,benchmark,benchmark_high,benchmark_low from product_base_info pbi 
where cp_id  = 7779904

-- 测试 info 
select bank_product_code  from product_base_info pbi 
where cp_id = 7732522

where issue_company_name  = '兰州银行' 



-- 测试持仓规模
select report_date,actual_scale,direct_scale from product_assets_pos_type pbi 
where cp_id  = 1391613
and primary_type = 99

-- 测试持仓
select * from product_assets_pos_type pbi 
where cp_id  = 7711817


-- 测试费率 
select * from product_fee_rate pfr 
where cp_id=7757394


-- 测试净值 
select nv.cp_id,trade_date ,
net_value ,accumulated_net_value ,yield_7_days_annual ,earning_per_ten_thousand from product_net_value nv 
join product_base_info info 
on info.cp_id = nv.cp_id 
where info.issue_company_type in (19, 20, 21, 22, 23)
and nv.cp_id = 7738510 
and nv.trade_date >='2022-07-10'
order by nv.trade_date  

select * from product_net_value
where cp_id  = 1391613

-- 测试规模表 
select * from product_share_scale
where cp_id = 1391613

-- 测试子分类 
select * from product_sub_type_dynamic 
where cp_id = 1269412

SET @now_date:= '2023-02-27';
select
		t.* 
	from
		(
		select
			A.cp_id, A.full_name, A.product_code, dy.report_date,
			case 
				when dy.product_type_son =1 then '纯固收'
				when dy.product_type_son =2 then '固收+'
				when dy.product_type_son =3 then '偏股混合'
				when dy.product_type_son =4 then '偏债混合'
			end as product_type_son,
			dy.asset_type,
			case 
				when dy.resource = 1 then '事前'
				when dy.resource = 2 then '事后'
			end as resource
		from
			product_base_info A
		left join product_sub_type_dynamic dy on
			A.cp_id = dy.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23)
			and dy.report_date <= @now_date
		order by
			report_date desc
		limit 10000000)t
	group by
		t.cp_id


-- 下载净值数据
select info.product_code as regis_code,
nv.cp_id as FinProCode,
nv.trade_date as EndDate,
nv.net_value as UnitNV,
nv.accumulated_net_value as AccumulatedUnitNV,
nv.yield_7_days_annual as LatestWeeklyYield ,
nv.earning_per_ten_thousand as DailyProfit
from product_net_value nv 
join product_base_info info 
on info.cp_id = nv.cp_id 
where info.issue_company_type in (19, 20, 21, 22, 23)
and nv.trade_date >='2023-07-01'


-- 下载业绩基准 
select * from (
select t.sub_cp_id,SUBSTRING_INDEX(t.sub_cp_id,'子份额:',-1) as a from (
select cp_id,sub_cp_id,issue_company_name,full_name ,product_code ,benchmark, product_series from product_base_info pbi 
where issue_company_type  in (19,20,21,22,23)
and sub_cp_id like '总份额:%,子份额%') t ) b
where instr (b.a,1396243)


-- 下载前十大
        select distinct info.product_code,ten_all.report_date,
        asset_name,asset_std_type,
        case 
            when ten_all.primary_type = 1 then '货币市场类'
            when ten_all.primary_type = 2 then '固定收益类'
            when ten_all.primary_type = 3 then '权益类'
            when ten_all.primary_type = 4 then '商品类'
            when ten_all.primary_type = 5 then '金融衍生品类'
            when ten_all.primary_type = 6 then '基金'
            when ten_all.primary_type = 7 then '资管产品'
            when ten_all.primary_type = 8 then '代客境外理财投资 qdii'
            when ten_all.primary_type = 9 then '新增可投资产'
            when ten_all.primary_type = 10 then '委外投资'
            when ten_all.primary_type = 11 then '另类资产'
            when ten_all.primary_type = 12 then '其他'
            when ten_all.primary_type = 99 then '合计'
        end as primary_type,three_level_type,
        asset_scale,actual_proportion from product_base_info info 
        left join  (select cp_id, report_date,asset_name,
        primary_type,secondary_type,three_level_type,
        asset_scale,actual_proportion,

        case 
            when project_name is not null then '非标' 
            else '标资'
        end as asset_std_type 
        from(
        select ten.*,nonstd.project_name from (
        select * from (select *, rank() 
        OVER (partition by product_code order by report_date desc) rank_num from (
        select * from (select x.product_code,y.* from product_base_info x 
        join product_assets_pos_top10 y on x.cp_id = y.cp_id )merge_info_asset
         where report_date <='2023-06-30')tt)a
        where a.rank_num =1) ten
        left join product_non_std_assets nonstd 
        on nonstd.cp_id = ten.cp_id
        and nonstd.report_date = ten.report_date
        and nonstd.project_name = ten.asset_name )tt) ten_all 
        on info.cp_id = ten_all.cp_id
        where info.issue_company_type in (19, 20, 21, 22, 23)
        
        


select * from (
select distinct info.cp_id,info.product_code,ten_all.report_date,
asset_name,asset_std_type,
case 
	when ten_all.primary_type = 1 then '货币市场类'
	when ten_all.primary_type = 2 then '固定收益类'
	when ten_all.primary_type = 3 then '权益类'
	when ten_all.primary_type = 4 then '商品类'
	when ten_all.primary_type = 5 then '金融衍生品类'
	when ten_all.primary_type = 6 then '基金'
	when ten_all.primary_type = 7 then '资管产品'
	when ten_all.primary_type = 8 then '代客境外理财投资 qdii'
	when ten_all.primary_type = 9 then '新增可投资产'
	when ten_all.primary_type = 10 then '委外投资'
	when ten_all.primary_type = 11 then '另类资产'
	when ten_all.primary_type = 12 then '其他'
	when ten_all.primary_type = 99 then '合计'
end as primary_type,three_level_type,
asset_scale,actual_proportion from product_base_info info 
left join  (select cp_id, report_date,asset_name,
primary_type,secondary_type,three_level_type,
asset_scale,actual_proportion,
sh_code,
sz_code,
other_generic_code,
case 
	when project_name is not null then '非标' 
	else '标资'
end as asset_std_type 
from(
select ten.*,nonstd.project_name from product_assets_pos_top10 ten
left join product_non_std_assets nonstd 
on nonstd.cp_id = ten.cp_id
and nonstd.report_date = ten.report_date
and nonstd.project_name = ten.asset_name)t ) ten_all 
on info.cp_id = ten_all.cp_id
where info.issue_company_type in (19, 20, 21, 22, 23)
and ten_all.report_date ='2023-06-30')


-- 下载资产配置表(最新)
                select distinct t.product_code as registration_code,
               t.report_date as end_date,
               t.primary_type as first_grade_type,
                case 
                when t.secondary_type = 1 then '现金及银行存款'
                when t.secondary_type = 2 then '同业存单'
                when t.secondary_type = 3 then '拆放同业及买入返售'
                when t.secondary_type = 4 then '债券'
                when t.secondary_type = 5 then '理财直接融资工具'
                when t.secondary_type = 6 then '非标准化债权类资产'
                when t.secondary_type = 7 then '股票'
                when t.secondary_type = 8 then '股权'
                when t.secondary_type = 9 then '银行机构'
                when t.secondary_type = 10 then '信托产品'
                when t.secondary_type = 11 then '证券公司'
                when t.secondary_type = 12 then '基金公司'
                when t.secondary_type = 13 then '期货公司'
                when t.secondary_type = 14 then '保险公司'
                when t.secondary_type = 15 then '公募基金'
                when t.secondary_type = 16 then '私募基金'
                when t.secondary_type = 17 then '其他'
                when t.secondary_type = -999 then t.primary_type
                when (t.primary_type is not null) then t.primary_type
                else null
            end as  second_grade_type,
            t.direct_scale as asset_before,
            t.direct_proportion as ratio_before,
            t.actual_scale as asset_after,
            t.actual_proportion as ratio_after
            from (
        select info.product_code,
                info.cp_id,
                pos.report_date,
              case 
                when pos.primary_type = 1 then '货币市场类'
                when pos.primary_type = 2 then '固定收益类'
                when pos.primary_type = 3 then '权益类'
                when pos.primary_type = 4 then '商品类'
                when pos.primary_type = 5 then '金融衍生品类'
                when pos.primary_type = 6 then '基金'
                when pos.primary_type = 7 then '资管产品'
                when pos.primary_type = 8 then 'qdii'
                when pos.primary_type = 9 then '新增可投资产'
                when pos.primary_type = 10 then '委外投资'
                when pos.primary_type = 11 then '另类资产'
                when pos.primary_type = 12 then '其他'
                when pos.primary_type = 99 then '合计'
            end as primary_type,
            secondary_type ,
            pos.direct_scale,
            direct_proportion,
            actual_scale,
            actual_proportion
              from (select * from (
            select *,rank() over(partition by product_code 
            order by  report_date desc )rank_num from 
            (select * from (select x.product_code,y.* from product_base_info x 
            join product_assets_pos_type y 
            on x.cp_id = y.cp_id) merge_info_asset
            where report_date <='2023-07-31')) tmp 
            where tmp.rank_num =1)pos
        left join product_base_info info
        on info.cp_id = pos.cp_id
        where info.issue_company_type in (19, 20, 21, 22, 23)) t

-- 下载资产配置表(某一个日期)
select distinct  t.product_code as 登记编码,
	   t.report_date as 公告日期,
	   t.primary_type as 一级资产,
		case 
	  	when t.secondary_type = 1 then '现金及银行存款'
	  	when t.secondary_type = 2 then '同业存单'
	  	when t.secondary_type = 3 then '拆放同业及买入返售'
	  	when t.secondary_type = 4 then '债券'
	  	when t.secondary_type = 5 then '理财直接融资工具'
	  	when t.secondary_type = 6 then '非标准化债权类资产'
	  	when t.secondary_type = 7 then '股票'
	  	when t.secondary_type = 8 then '股权'
	  	when t.secondary_type = 9 then '银行机构'
	  	when t.secondary_type = 10 then '信托产品'
	  	when t.secondary_type = 11 then '证券公司'
	  	when t.secondary_type = 12 then '基金公司'
	  	when t.secondary_type = 13 then '期货公司'
	  	when t.secondary_type = 14 then '保险公司'
	  	when t.secondary_type = 15 then '公募基金'
	  	when t.secondary_type = 16 then '私募基金'
	  	when t.secondary_type = 17 then '其他'
	  	when t.secondary_type = -999 then t.primary_type
		when (t.primary_type is not null) then t.primary_type
		else null
	end as  二级资产,
	t.direct_scale as 穿透前规模,
	t.direct_proportion as 穿透前规模占比,
	t.actual_scale as 穿透后规模,
	t.actual_proportion as 穿透后规模占比
	from (
select distinct info.product_code,
		pos.report_date,
	  case 
	  	when pos.primary_type = 1 then '货币市场类'
	  	when pos.primary_type = 2 then '固定收益类'
	  	when pos.primary_type = 3 then '权益类'
	  	when pos.primary_type = 4 then '商品类'
	  	when pos.primary_type = 5 then '金融衍生品类'
	  	when pos.primary_type = 6 then '基金'
	  	when pos.primary_type = 7 then '资管产品'
	  	when pos.primary_type = 8 then 'qdii'
	  	when pos.primary_type = 9 then '新增可投资产'
	  	when pos.primary_type = 10 then '委外投资'
	  	when pos.primary_type = 11 then '另类资产'
	  	when pos.primary_type = 12 then '其他'
	  	when pos.primary_type = 99 then '合计'
	end as primary_type,
	secondary_type ,
	pos.direct_scale,
	direct_proportion,
	actual_scale,
	actual_proportion
	  from  product_assets_pos_type pos
left join product_base_info info
on info.cp_id = pos.cp_id
where info.issue_company_type in (19, 20, 21, 22, 23)
and pos.report_date='2023-06-30') t


select * from (select *, rank() 
OVER (partition by report_date order by report_date desc) rank_num from product_assets_pos_top10)a
where a.rank_num =1  


select * from product_assets_pos_type pos 
where cp_id = 1405407

select
	info.*
from
	product_base_info info
	
-- 成农商行的资产数据 
select issue_company_name,sum(asset_value) from(
select
	info.cp_id,
	info.issue_company_name,product_code,
	info.classify_type,
	info.actual_end_date,
	asset.report_date,
	case 
		when asset.actual_scale is not null then asset.actual_scale
		when asset.actual_scale is null then asset.direct_scale
	end as asset_value
from
	product_base_info info
left join (
	select
		*
	from
		(
		select
			*, rank() over(partition by cp_id
		order by
			report_date desc )rank_num
		from
			product_assets_pos_type) tmp
	where
		tmp.rank_num = 1) asset
on info.cp_id = asset.cp_id
where (info.actual_end_date >= '2023-04-10' or info.actual_end_date is null ) 
and info.issue_company_type in (3, 4)
-- and info.issue_company_name ='兰州银行'
and asset.primary_type = 99 
and info.classify_type in (1,3) )  t 
group by issue_company_name




select
	info.cp_id,
	info.issue_company_name,product_code,
	info.classify_type,
	info.actual_end_date,
	asset.report_date,
	case 
		when asset.actual_scale is not null then asset.actual_scale
		when asset.actual_scale is null then asset.direct_scale
	end as asset_value
from
	product_base_info info
left join (
	select
		*
	from
		(
		select
			*, rank() over(partition by cp_id
		order by
			report_date desc )rank_num
		from
			product_assets_pos_type) tmp
	where
		tmp.rank_num = 1) asset
on info.cp_id = asset.cp_id
where info.issue_company_name ='兰州银行'
and asset.primary_type = 99 
order by info.actual_end_date desc

where (info.actual_end_date >= '2023-04-10' or info.actual_end_date is null ) 
and info.issue_company_type in (3, 4)
-- and info.issue_company_name ='兰州银行'
and asset.primary_type = 99 
and info.classify_type in (1,3)



-- 验证民生理财
select
	   t.cp_id, t.full_name, t.product_code , t.report_date, t.actual_scale,
	   t.direct_scale 
	from
		(
		select
			A.cp_id, A.full_name, A.product_code, asset.report_date,asset.actual_scale, asset.direct_scale
		from
			product_base_info A
		left join 
		(select * from(
		select *, rank() over(partition by cp_id
		order by
			report_date desc )rank_num
		from
			product_assets_pos_type) tmp
	where
		tmp.rank_num = 1) asset on
			A.cp_id = asset.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23)
			and asset.primary_type = 99
			and asset.report_date <= '2022-12-31'
	      )t
    where t.cp_id = 7734719

-- 基金投资字段 

select * from product_open_net_cycle ponc 

-- 周度规模数据

select cp_id,trade_date,open_duration_scale ,open_duration_share ,
duration_scale_type ,duration_share_type from product_share_scale a
where a.trade_date >'2023-01-01'

-- 到期收益率数据 
select info.product_code,info.full_name ,
info.issue_company_name ,
info.invest_start_date as prodcut_establish_date,
case 
	when info.actual_end_date is not null then info.actual_end_date
	else info.invest_end_date 
end as product_maturity_date,
ytm.cp_id,
ytm.invest_start_date,
ytm.invest_end_date ,
ytm.is_open,
ytm.initial_net_value ,
ytm.end_acc_net_value ,
ytm.benchmark,
ytm.actual_yield_record ,
ytm.actual_yield_calculate ,
ytm.data_source 
from product_product_ytm ytm 
left join product_base_info info 
on ytm.cp_id = info.cp_id 
where ytm.invest_end_date <='2023-06-30'
and ytm.invest_end_date >='2023-01-01'
and info.issue_company_type  in (19,20,21,22,23)

select * from product_product_ytm ppy 
where cp_id = 1176724


select * from product_net_value pnv 
where cp_id =7736461


- new_bank

--  普益 bank_wealth_product 表 

SET @now_date:= '2023-06-30';


SET @type_now_date:= '2023-06-30';

select
	issue_company_name as CompanyName,
	parent_bank as ParentCompName,
	case
		when issue_company_type = 19 then '国有行全资理财子公司'
		when issue_company_type = 20 then '股份制行全资理财子公司'
		when issue_company_type = 21 then '城商行全资理财子公司'
		when issue_company_type = 22 then '农村金融机构全资理财子公司'
		when issue_company_type = 23 then '合资理财子公司'
		else '其它机构'
	end as ParentCompType,
	-- EstablishmentDate 
 info.cp_id as FinProCode,
	info.full_name as product_name,
	case
		when (info.sale_start_date > now()) then '预售期'
		when (info.sale_end_date >= now()) & (info.sale_start_date <= now()) then '募集期'
		when (coalesce(info.actual_end_date, info.invest_end_date , "") >= now()) & (info.invest_start_date <= now()) then '运行期'
		when (coalesce(info.actual_end_date, info.invest_end_date , "") < now()) then '已到期'
		else ''
	end as SecuState,
	sale_start_date as PopularizeStDate,
	case
		when (raise_way = 1 ) then '公募'
		when (raise_way = 2) then '私募'
	end as RaisingType,
	case
		when (open_type = 0 ) & (is_net_value = 1) then '封闭式净值型'
		when (open_type = 0 ) & (is_net_value = 0) then '封闭式非净值型'
		when (open_type in (1, 2, 6, 7, 8, 9, 10)) & (is_net_value = 1) then '开放式净值型'
		when (open_type in (1, 2, 6, 7, 8, 9, 10)) & (is_net_value = 0) then '开放式非净值型'
		else ''
	end as OperationType,
	case
		when (is_cash_manage = 1) then '现金管理类'
		when (product_type = 1) then '固定收益类'
		when (product_type = 2) then '权益类'
		when (product_type = 3) then '商品及金融衍生品类'
		when (product_type = 4) then '混合类'
		else ''
	end as InvestmentType,
	AssetData.report_date as EndDate,
	coalesce(AssetData.asset_scale * 10000, info.actual_raise_scale, "") as AssetValue,
	-- replace(SUBSTRING_INDEX(sub_cp_id, ',', 1), '总份额:', '') as main,
 case
		when sub_cp_id is null then '产品'
		when replace(SUBSTRING_INDEX(sub_cp_id, ',', 1), '总份额:', '') = info.cp_id then '母产品'
		else '子产品'
	end as ProductType,
	invest_start_date as product_establish_date,
	invest_currency,
	case
		when (invest_currency = 'CNY') then '人民币'
		when (invest_currency = 'USD') then '美元'
		when (invest_currency = 'HKD') then '港元'
		when (invest_currency = 'AUD' )then '美元'
		when (invest_currency = 'GBP' )then '英镑'
		when (invest_currency = 'EUR' )then '欧元'
		when (invest_currency = 'JPY' )then '日元'
		when (invest_currency = 'CHF' )then '瑞士法郎'
		when (invest_currency = 'CAD' )then '加拿大元'
		when (invest_currency = 'SGD' )then '新加坡元'
		when (invest_currency = 'CHF' )then '新加坡元'
		when (invest_currency = 'NZD' )then '新西兰元'
		when (invest_currency = 'SEK' )then '瑞典克朗'
		else ''
	end as CurrencyUnit,
	short_name as SecuAbbr,
	min_hold_term as MinInvestTerm,
	'日' as MinInvestTermUnit,
	case
		when (risk_level = 1) then '低'
		when (risk_level = 2) then '中低'
		when (risk_level = 3) then '中'
		when (risk_level = 4) then '中高'
		when (risk_level = 5) then '高'
	end as RiskLevel,
	benchmark as Benchmark,
	benchmark_high as BenchmarkMax,
	benchmark_low as BenchmarkMin,
	fee.manage_fee,
	fee.carry_fee,
	fee.sale_fee,
	-- fee.num,
 coalesce(actual_end_date, invest_end_date, "") as MaturityDate,
	is_cash_manage as inv_type,
	info.product_code as RegistrationCode,
	is_structure as IfStructure,
	case
		when (invest_term = '无固定期限') then 999999
		when (invest_term is not null ) then invest_term
		else null
	end as InvestTerm,
	product_series,
	transfer_date,
	trustee_bank,
	case 
		when (profit_type = 1) then '保证收益型'
		when (profit_type = 2) then '保本浮动收益型'
		when (profit_type = 3) then '非保本浮动收益型'
	end as profit_type,
	case 
		when(info.classify_type =1) then '总份额'
		when(info.classify_type =2) then '子份额'
		else '不区分'
	end as classify_type,
	info.customer_type as IssueObject,
	case 
		when (info.open_type = 0) then '封闭式'
		when (info.open_type = 1) then '定活两便型'
		when (info.open_type = 2) then '每日开放型'
		when (info.open_type = 6) then '客户周期型'
		when (info.open_type = 7) then '定开型(申赎同期)'
		when (info.open_type = 8) then '定开型(申赎不同期)'
		when (info.open_type = 9) then '最小持有期型'
		when (info.open_type = 10) then '其他半开型'
	end as open_type,
	info.open_rules,
	info.fixed_income_upper,
	info.fixed_income_lower,
	info.equity_upper,
	info.equity_lower,
	info.derivatives_upper,
	info.derivatives_lower,
	info.invest_strategy,
	info.top_raise_scale,
	info.actual_raise_scale,
	info.is_index ,
	info.is_early_redeem,
	info.old_invest_scope,
	product_type_table.report_date,
	product_type_table.product_type_son,
	product_type_table.asset_type,
	product_type_table.resource
from
	product_base_info info
left join (
	select
		t.cp_id, t.full_name, t.product_code , t.report_date, 
		coalesce(t.direct_scale ,t.actual_scale, "") as asset_scale
	from
		(
		select
			A.cp_id, A.full_name, A.product_code,
			asset.report_date, asset.actual_scale, 
			asset.direct_scale
		from
			product_base_info A
		left join (select * from(
		select *, rank() over(partition by cp_id
		order by
			report_date desc )rank_num
		from
			(select * from product_assets_pos_type
			where report_date <= @now_date)) tmp
	where
		tmp.rank_num = 1) asset on
			A.cp_id = asset.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23)
			and asset.primary_type = 99)t) AssetData on
	info.cp_id = AssetData.cp_id
left join (
	select
		t.cp_id, avg(t.fixed_manage_fee_rate) as manage_fee , avg(t.variable_manage_fee_rate) as carry_fee, avg(t.sale_fee_rate) as sale_fee, count(*) as num
	from
		(
		select
			info.full_name, info.product_code , fee.*
		from
			product_fee_rate fee
		join product_base_info info on
			fee.cp_id = info.cp_id
		where
			info.issue_company_type in (19, 20, 21, 22, 23)
			and fee.fee_end_date >= @type_now_date
			and fee.fee_start_date <= @type_now_date) t
	group by
		t.cp_id) fee on
	info.cp_id = fee.cp_id
left join (
select
		t.* 
	from
		(
		select
			A.cp_id, A.full_name, A.product_code, dy.report_date,
			case 
				when dy.product_type_son =1 then '纯固收'
				when dy.product_type_son =2 then '固收+'
				when dy.product_type_son =3 then '偏股混合'
				when dy.product_type_son =4 then '偏债混合'
			end as product_type_son,
			dy.asset_type,
			case 
				when dy.resource = 1 then '事前'
				when dy.resource = 2 then '事后'
			end as resource
		from
			product_base_info A
		left join (
			select * from (
				select * ,rank() over (partition by cp_id order by report_date desc) rank_num 
				from (
				select * from product_sub_type_dynamic
				where report_date <= @type_now_date))tmp_dy
				where tmp_dy.rank_num = 1)dy on
			A.cp_id = dy.cp_id
		where
			A.issue_company_type in (19, 20, 21, 22, 23))t) product_type_table
		on  info.cp_id = product_type_table.cp_id
where
	info.issue_company_type in (19, 20, 21, 22, 23)

	
-- 封闭产品到期收益率兑付情况 
	
select 
	pbi.issue_company_name,
	pbi.product_code,
	pbi.full_name,
	pbi.invest_term,
	CEILING(pbi.invest_term / 30.4) as invest_term_m,
	ppy.cp_id,
	ppy.invest_start_date,
	ppy.invest_end_date,
	actual_yield_record,
	actual_yield_calculate,
	case 
		when actual_yield_record is null then actual_yield_calculate
		else actual_yield_record
	end as acutal_yield,
	case 
		when actual_yield <2 then 1 -- 有问题
		else 0
	end as less_than_2,
	case 
		when actual_yield > 3 then 1 
		else 0 
	end as more_than_3,
	data_source
from
	product_product_ytm ppy
left join product_base_info pbi 
on ppy.cp_id = pbi.cp_id 
where
	is_open = 0
	and ppy.invest_end_date >= '2023-01-01'
	and ppy.invest_end_date <= '2023-08-31'
	and pbi.issue_company_name in('工银理财','农银理财','中银理财','建信理财','交银理财','招银理财','兴银理财','信银理财','光大理财')
order by invest_term_m

select * from product_net_value pnv 
where cp_id =7723710

select * from product_product_ytm  pnv 
where cp_id =7723710




	      