# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 14:54 
# @Author    : Wangyd5 
# @File      : sql
# @Project   : licai
# @Function  ：
# --------------------------------
import datetime
today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)


# fixme 普益日期参数还没更改好
class SqlStatement:

    py_sql_bank: str = """ 
    
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
        case
            when(info.customer_type =1) then '一般客户'
            when(info.customer_type =2) then '私人银行'
            when(info.customer_type =3) then '高净值客户'
            else '不区分'
        end as IssueObject,
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
        info.benchmark,
        case
            when info.product_object =1 then '个人'
            when info.product_object =2 then '机构'
            when info.product_object =3 then '个人和机构'
            when info.product_object =4 then '机构'
            when info.product_object =5 then '机构'
            when info.product_object =6 then '个人和机构'
        end as product_object
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
                where report_date <= '%s')) tmp
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
                and fee.fee_end_date >= '%s'
                and fee.fee_start_date <= '%s') t
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
                    where report_date <= '%s'))tmp_dy
                    where tmp_dy.rank_num = 1)dy on
                A.cp_id = dy.cp_id
            where
                A.issue_company_type in (19, 20, 21, 22, 23))t) product_type_table
            on  info.cp_id = product_type_table.cp_id
    where
        info.issue_company_type in (19, 20, 21, 22, 23);
    
        """ %(today,today,today,today)   # 资产配置，费率，费率，分类类型


    jy_2_test :str = "SELECT * from FP_BasicInfo where FinProCode ='SEC00003JDSI' "


    jy_sql_bank:str = f"""
        DECLARE @code date
        set @code = '{today}'
        SELECT
            DISTINCT A.AgentName as CompanyName,
            D.ChiName as ParentCompName,
            E.QualName as ParentCompType,
            C.EstablishmentDate,
            B.FinProCode ,
            B.ChiName as product_name,
            G.ChiName as SecuState,
            F.PopularizeStDate,
            case
                when F.MinInvestDay is null
                or F.MinInvestDay = -1
                or F.OperationType is null then '数据缺失'
                when (F.OperationType = 'FCC0000001T4')
                and (F.MinInvestDay <= 370) then '封闭短期'
                when (F.OperationType = 'FCC0000001T4')
                and (F.MinInvestDay > 370)
                and (F.MinInvestDay <= 1105) then '封闭中期'
                when (F.OperationType = 'FCC0000001T4')
                and (F.MinInvestDay > 1105) then '封闭长期'
                when (F.OperationType = 'FCC0000001T6')
                and (F.MinInvestDay <= 31) then '开放短期'
                when (F.OperationType = 'FCC0000001T6')
                and (F.MinInvestDay > 31)
                and (F.MinInvestDay <= 93) then '开放短中期'
                when (F.OperationType = 'FCC0000001T6')
                and (F.MinInvestDay > 93)
                and (F.MinInvestDay <= 186) then '开放中期'
                when (F.OperationType = 'FCC0000001T6')
                and (F.MinInvestDay > 186)
                and (F.MinInvestDay <= 370) then '开放中长期'
                when (F.OperationType = 'FCC0000001T6')
                and (F.MinInvestDay > 370) then '开放长期'
                else '其他'
            end as MinInvestTimeType,
            H.ChiName as RaisingType,
            I.ChiName as OperationType,
            J.ChiName as InvestmentType,
            COALESCE(AssetAllocation.EndDate, net_value_nv.EndDate) as EndDate,
            case
                when AssetAllocation.AssetValue is not null then AssetAllocation.AssetValue
                when net_value_nv.NV is not null then net_value_nv.NV
                else F.ActRaisingAmount * 100000000
            end as AssetValue,
            AssetAllocation.AssetPublDateIndex,
            case
                when CodeRelationship.FinProCode is not null then '子产品'
                when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
                when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
                when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
                else '产品'
            end as ProductType,
            F.EstablishmentDate as product_establish_date,
            K.ChiName as CurrencyUnit,
            B.SecuAbbr,
            F.MinInvestTerm,
            L.ChiName as MinInvestTermUnit,
            M.ChiName as RiskLevel,
            F.BenchmarkMax,
            F.BenchmarkMin,
            F.IssueObject,
            fee.manage_fee,
            fee.manage_fee_unit,
            fee.carry_fee,
            fee.carry_fee_unit,
            case
                when F.ActMaturityDate is not null then F.ActMaturityDate
                else F.MaturityDate
            end as MaturityDate,
            case
                when F.InvestmentType = 'FCC0000001T8' then
                case
                    when B.ChiName like '%现金%' then 1
                    else
                    case
                        when F.MinInvestDay = 1 then
                        case
                            when A.AgentName = '中银理财有限责任公司'
                            and B.ChiName like '%乐享%' then 1
                            when A.AgentName = '建信理财有限责任公司'
                            and (B.ChiName like '%龙宝%'
                            or B.ChiName like '%建信宝%'
                            or B.ChiName like '%安鑫%'
                            or B.ChiName like '%恒赢%'
                            or B.ChiName like '%净鑫%'
                            or B.ChiName like '%净利%'
                            or B.ChiName like '%天天利%' ) then 1
                            when A.AgentName = '交银理财有限责任公司'
                            and (B.ChiName like '%现金添利%'
                            or B.ChiName like '%悦享%' ) then 1
                            when A.AgentName = '农银理财有限责任公司'
                            and B.ChiName like '%时时付%' then 1
                            when A.AgentName = '工银理财有限责任公司'
                            and B.ChiName like '%添利宝%' then 1
                            when A.AgentName = '光大理财有限责任公司'
                            and B.ChiName like '%阳光碧%' then 1
                            when A.AgentName = '招银理财有限责任公司'
                            and (B.ChiName like '%日日欣%'
                            or B.ChiName like '%朝招金%'
                            or B.ChiName like '%开鑫宝%' ) then 1
                            when A.AgentName = '兴银理财有限责任公司'
                            and B.ChiName like '%添利%' then 1
                            when A.AgentName = '杭银理财有限责任公司'
                            and (B.ChiName like '%新钱包%'
                            or B.ChiName like '%金钱包%'
                            or B.ChiName like '%臻钱包%' ) then 1
                            when A.AgentName = '宁银理财有限责任公司'
                            and( B.ChiName like '%宁欣天天鎏金%'
                            or B.ChiName like '%天利鑫%' ) then 1
                            when A.AgentName = '徽银理财有限责任公司'
                            and B.ChiName like '%天天盈%' then 1
                            when A.AgentName = '南银理财有限责任公司'
                            and B.ChiName like '%添睿%' then 1
                            when A.AgentName = '苏银理财有限责任公司'
                            and B.ChiName like '%启源%' then 1
                            when A.AgentName = '平安理财有限责任公司'
                            and B.ChiName like '%天天成长%' then 1
                            when A.AgentName = '青银理财有限责任公司'
                            and B.ChiName like '%奋斗%' then 1
                            when A.AgentName = '渝农商理财有限责任公司'
                            and B.ChiName like '%渝快宝%' then 1
                            when A.AgentName = '信银理财有限责任公司'
                            and B.ChiName like '%日盈象%' then 1
                            when A.AgentName = '广银理财有限责任公司'
                            and B.ChiName like '%鎏金%' then 1
                            when A.AgentName = '民生理财有限责任公司'
                            and B.ChiName like '%天天增利%' then 1
                            when A.AgentName = '恒丰理财有限责任公司'
                            and B.ChiName like '%新恒梦钱包%' then 1
                            when A.AgentName = '中邮理财有限责任公司'
                            and (B.ChiName like '%零钱宝%'
                            or B.ChiName like '%理财宝%') then 1
                            else 0
                        end
                        else 0
                    end
                end
                else 0
            end as inv_type,
            F.RegistrationCode,
            lever.lever_date,
            lever.leverage,
            manager.ChiName as manage_comp,
            F.MinInvestDay,
            fi.ChiName as IfStructure,
            F.InvestTerm,
            F.InvestTermUnit,
            F.ActRaisingAmount * 100000000 as ActRaisingAmount
        FROM
            (
            select
                *
            from
                LC_InstiQualCoRe
            where
                QualCode in (2029)) A
            -- 银行理财子
        left JOIN (
            SELECT
                *
            FROM
                FP_SecuMain
            WHERE
                SecuCategory = 'FCC0000001TD' ) B ON
            B.CompanyCode = A.CompanyCode
        left JOIN LC_InstiArchive C ON
            A.CompanyCode = C.CompanyCode
        left join LC_InstiArchive D on
            D.CompanyCode = C.ParentCompany
        left JOIN (
            select
                *
            from
                LC_InstiQualCoRe
            where
                QualCode in (2004, 2007, 2008, 2015, 2029) )E
            -- 规定母公司类别  城商行、国有行、外资合营的划分等 
         on
            D.CompanyCode = E.CompanyCode
        left JOIN (
            select
                *,
                CASE
                    when MinInvestTermUnit is null
                    or MinInvestTerm is null then -1
                    when MinInvestTermUnit = 'FCC0000001S9' then MinInvestTerm
                    when MinInvestTermUnit = 'FCC0000001TC' then MinInvestTerm * 7
                    when MinInvestTermUnit = 'FCC0000001S8' then MinInvestTerm * 30
                    when MinInvestTermUnit = 'FCC0000001S7' then MinInvestTerm * 365
                    else -1
                end as MinInvestDay
            from
                FP_BasicInfo ) F on
            B.FinProCode = F.FinProCode
        left JOIN FP_Indicator G on
            B.SecuState = G.GilCode
        left JOIN FP_Indicator H on
            F.RaisingType = H.GilCode
        left JOIN FP_Indicator I on
            F.OperationType = I.GilCode
        left JOIN FP_Indicator J on
            F.InvestmentType = J.GilCode
        left JOIN FP_Indicator K on
            F.CurrencyUnit = K.GilCode
        left join FP_Indicator L on
            F.MinInvestTermUnit = L.GilCode
        left join FP_Indicator M on
            F.RiskLevelCode = M.GilCode
        left join (
            select
                COALESCE(manage.FinProCode, carry.FinProCode) as FinProCode, carry.carry_fee, carry.carry_fee_unit , manage.manage_fee, manage.manage_fee_unit
            from
                (
                select
                    *
                from
                    (
                    select
                        FinProCode as FinProCode, ChargeRate as carry_fee, dd.ChiName as carry_fee_unit, ROW_NUMBER() over(PARTITION by FinProCode
                    ORDER BY
                        FP_ChargeRate.CancelDate DESC) as date_index
                    from
                        FP_ChargeRate
                    left join dbo.FP_Indicator dd on
                        FP_ChargeRate.ChargeRateUnit = dd.GilCode
                    where
                        FP_ChargeRate.ChargeRateType = 'FCC0000001RX'
                        and FP_ChargeRate.ExcuteDate <= @code
                        and FP_ChargeRate.CancelDate >= @code
                        and FP_ChargeRate.ChargeRate is not null ) carry_1
                where
                    carry_1.date_index = 1) carry
            FULL join (
                select
                    *
                from
                    (
                    select
                        FinProCode, ChargeRate as manage_fee, ee.ChiName as manage_fee_unit, ROW_NUMBER() over(PARTITION by FinProCode
                    ORDER BY
                        FP_ChargeRate.CancelDate DESC) as date_index
                    from
                        FP_ChargeRate
                    left join dbo.FP_Indicator ee on
                        FP_ChargeRate.ChargeRateUnit = ee.GilCode
                    where
                        FP_ChargeRate.ChargeRateType = 'FCC0000001RU'
                        and FP_ChargeRate.ChargeRateInterval = 'FCC0000001SF'
                        and FP_ChargeRate.ExcuteDate <= @code
                        and FP_ChargeRate.CancelDate >= @code)manage1
                where
                    manage1.date_index = 1) manage on
                manage.FinProCode = carry.FinProCode )fee on
            B.FinProCode = fee.FinProCode
        left join (
            select
                FinProCode, AssetTypeCode, EndDate as EndDate, MarketValue as AssetValue, ROW_NUMBER() over(PARTITION by FinProCode
            ORDER BY
                InfoPublDate desc, AssetTypeCode) as AssetPublDateIndex
            from
                (
                select
                    *
                from
                    FP_AssetAllocation
                where
                    -- 金融产品净资产或者总资产
         AssetTypeCode in ('FCC0000001X9', 'FCC0000001XA')
                    -- 非空的市值
                    and MarketValue is not null
                    and EndDate <= @code)ttt) AssetAllocation on
            AssetAllocation.FinProCode = B.FinProCode
        left join (
            select
                *
            from
                FP_CodeRelationship
            where
                CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) CodeRelationship on
            B.FinProCode = CodeRelationship.FinProCode
        left join (
            select
                *
            from
                FP_CodeRelationship
            where
                CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) RelatedCodeRelationship on
            B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
        left join (
            select
                *
            from
                FP_CodeRelationship
            where
                CodeDefine = 'FCC000000YDD') CodeRelationship_fenqi on
            B.FinProCode = CodeRelationship_fenqi.FinProCode
        left join (
            select
                *
            from
                FP_CodeRelationship
            where
                CodeDefine = 'FCC00000129X') CodeRelationship_fenqixian on
            B.FinProCode = CodeRelationship_fenqixian.FinProCode
        left join (
            select
                FinProCode, EndDate as lever_date , leverage
            from
                (
                select
                    FinProCode , EndDate , leverage , ROW_NUMBER() over(PARTITION by FinProCode
                ORDER BY
                    c.EndDate DESC) as date_index
                from
                    (
                    select
                        COALESCE (a.FinProCode, b.FinProCode) as FinProCode, COALESCE (a.EndDate, b.EndDate) as EndDate, all_value_sum / net_value_sum as leverage
                    from
                        (
                        select
                            FinProCode, EndDate, MarketValue as net_value_sum
                        from
                            dbo.FP_AssetAllocation
                        where
                            AssetTypeCode = 'FCC0000001X9'
                            and SecuCategory = 'FCC0000001TD') a
                    join (
                        select
                            FinProCode, EndDate, MarketValue as all_value_sum
                        from
                            dbo.FP_AssetAllocation
                        where
                            AssetTypeCode = 'FCC0000001XA'
                            and SecuCategory = 'FCC0000001TD') b on
                        a.FinProCode = b.FinProCode
                        and a.EndDate = b.EndDate )c) t
            where
                t.date_index = 1 ) lever on
            B.FinProCode = lever.FinProCode
        left join LC_InstiArchive manager on
            B.CompanyCode = manager.CompanyCode
        left join FP_Indicator fi on
            F.IfStructure = fi.GilCode
        left join (
            select
                FinProCode, EndDate, NV
            from
                (
                select
                    FinProCode, EndDate, NV, ROW_NUMBER() over(PARTITION by FinProCode
                order by
                    EndDate desc ) as num
                from
                    dbo.FP_NetValue ) fnv
            where
                fnv.num = 1
                and fnv.NV is not null)net_value_nv on
            net_value_nv.FinProCode = B.FinProCode
        where
            (AssetAllocation.AssetPublDateIndex = 1
            or AssetAllocation.AssetPublDateIndex is null) 
            """

    sql_py_asset_portfolio = """
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
            where report_date <= '%s')) tmp 
            where tmp.rank_num =1)pos
        left join product_base_info info
        on info.cp_id = pos.cp_id
        where info.issue_company_type in (19, 20, 21, 22, 23)) t
        """ % (today)

    sql_py_top_10 = """
    
        select distinct info.product_code as registration_code,
        ten_all.report_date as end_date,
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
        join  (select cp_id, report_date,asset_name,
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
        select * from (select a.product_code,b.* from product_base_info a 
        join product_assets_pos_top10 b on a.cp_id = b.cp_id )merge_info_asset
         where report_date <='%s' )tt)a
        where a.rank_num =1) ten
        left join product_non_std_assets nonstd 
        on nonstd.cp_id = ten.cp_id
        and nonstd.report_date = ten.report_date
        and nonstd.project_name = ten.asset_name )tt) ten_all 
        on info.cp_id = ten_all.cp_id
        where info.issue_company_type in (19, 20, 21, 22, 23)
    """ % (today)

    sql_prodcut_buy = """
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
        product_type_table.resource,
        subscription_start_date,
        subscription_end_date
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
                where report_date <= current_date())) tmp
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
                and fee.fee_end_date >=current_date()
                and fee.fee_start_date <= current_date()) t
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
                    where report_date <= current_date()))tmp_dy
                    where tmp_dy.rank_num = 1)dy on
                A.cp_id = dy.cp_id
            where
                A.issue_company_type in (19, 20, 21, 22, 23))t) product_type_table
            on  info.cp_id = product_type_table.cp_id
    left join (
        select cp_id,subscription_start_date,subscription_end_date from   product_open_net_cycle) cy 
    on cy.cp_id =info.cp_id 
    where
        info.issue_company_type in (19, 20, 21, 22, 23)
        and  DATEDIFF(subscription_end_date,current_date()) >10
    """