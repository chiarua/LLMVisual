import { QueryConfig } from './config';
import { SpecQueryModel } from './model';
import { EncodingQuery } from './query/encoding';
import { Schema } from './schema';
import { Dict } from './util';
export declare function stylize(answerSet: SpecQueryModel[], schema: Schema, opt: QueryConfig): SpecQueryModel[];
export declare function smallRangeStepForHighCardinalityOrFacet(specM: SpecQueryModel, schema: Schema, encQIndex: Dict<EncodingQuery>, opt: QueryConfig): SpecQueryModel;
export declare function nominalColorScaleForHighCardinality(specM: SpecQueryModel, schema: Schema, encQIndex: Dict<EncodingQuery>, opt: QueryConfig): SpecQueryModel;
export declare function xAxisOnTopForHighYCardinalityWithoutColumn(specM: SpecQueryModel, schema: Schema, encQIndex: Dict<EncodingQuery>, opt: QueryConfig): SpecQueryModel;
